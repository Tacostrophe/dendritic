from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class AbstractSlugFromName(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # creating new model => adding slug
        if not self.slug:
            self.slug = slugify(self.name)
        return super(AbstractSlugFromName, self).save(*args, **kwargs)


class Menu(AbstractSlugFromName):
    def __str__(self):
        return f'Menu: {self.slug}'


class Node(AbstractSlugFromName):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='nodes',
        null=False,
        blank=False
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child',
        null=True,
        blank=True,
    )
    relatives = models.ManyToManyField(
        'self',
        through='Relations',
    )

    def __str__(self):
        return self.slug

#     def get_absolute_url(self):
#         return
#
    def clean(self, *args, **kwargs):
        # validate self_menu == parent_menu
        if (self.parent):
            if (self.parent.menu != self.menu):
                raise ValidationError(
                    _('Node and it\'s parent should be in the same menu' +
                      '(%(self_menu)s != %(parent_menu)s)'),
                    code='invalid',
                    params={
                        'self_menu': self.menu,
                        'parent_menu': self.parent.menu,
                    }
                )
        return super(Node, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        data = super(Node, self).save(*args, **kwargs)
        # create node's relations
        if (self.parent):
            grandpa = self.parent.parent
            print(f'{grandpa=}')
            if (grandpa):
                ancestor_list = [Relations(descendant=self, ancestor=grandpa)]
                print(self.parent.ancestors)
                for relations in self.parent.ancestors.all():
                    ancestor_list.append(Relations(
                        descendant=self,
                        ancestor=relations.ancestor
                    ))
                print(f'{ancestor_list=}')
                Relations.objects.bulk_create(ancestor_list)
        return data
#
#     def delete(self):


class Relations(models.Model):
    '''Relations between nodes that have at least one node between them'''
    ancestor = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='descendants',
    )
    descendant = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='ancestors',
    )

    def __str__(self):
        return f'{self.ancestor}=>{self.descendant}'

from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import validate_slug
from django.core.validators import validate_unicode_slug
from django.db import models
from django.urls import reverse


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', blank=True)
    cooking_times = models.ManyToManyField('CookingTime', blank=True)
    ingredients = models.ManyToManyField('Ingredient', blank=True)
    instructions = models.ManyToManyField('Instruction', blank=True)
    images = models.ManyToManyField('Image', blank=True)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)
    comments = models.ManyToManyField('Comment', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_recipe', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_recipe', args=[str(self.id)])

    def get_add_ingredient_url(self):
        return reverse('add_ingredient', args=[str(self.id)])

    def get_add_instruction_url(self):
        return reverse('add_instruction', args=[str(self.id)])

    def get_add_image_url(self):
        return reverse('add_image', args=[str(self.id)])

    def get_add_tag_url(self):
        return reverse('add_tag', args=[str(self.id)])

    def get_add_category_url(self):
        return reverse('add_category', args=[str(self.id)])

    def get_add_cooking_time_url(self):
        return reverse('add_cooking_time', args=[str(self.id)])

    def get_add_author_url(self):
        return reverse('add_author', args=[str(self.id)])

    def get_delete_ingredient_url(self, ingredient_id):
        return reverse('delete_ingredient', args=[str(self.id), str(ingredient_id)])

    def get_delete_instruction_url(self, instruction_id):
        return reverse('delete_instruction', args=[str(self.id), str(instruction_id)])

    def get_delete_image_url(self, image_id):
        return reverse('delete_image', args=[str(self.id), str(image_id)])

    def get_delete_tag_url(self, tag_id):
        return reverse('delete_tag', args=[str(self.id), str(tag_id)])

    def get_delete_category_url(self, category_id):
        return reverse('delete_category', args=[str(self.id), str(category_id)])

    def get_delete_cooking_time_url(self, cooking_time_id):
        return reverse('delete_cooking_time', args=[str(self.id), str(cooking_time_id)])

    def get_delete_author_url(self, author_id):
        return reverse('delete_author', args=[str(self.id), str(author_id)])

    def get_ingredients(self):
        return self.ingredients.all()

    def get_instructions(self):
        return self.instructions.all()

    def get_images(self):
        return self.images.all()

    def get_tags(self):
        return self.tags.all()

    def get_categories(self):
        return self.categories.all()

    def get_cooking_times(self):
        return self.cooking_times.all()

    def get_authors(self):
        return self.authors.all()

    def get_ingredients_count(self):
        return self.ingredients.count()

    def get_instructions_count(self):
        return self.instructions.count()

    def get_images_count(self):
        return self.images.count()

    def get_tags_count(self):
        return self.tags.count()

    def get_categories_count(self):
        return self.categories.count()

    def get_cooking_times_count(self):
        return self.cooking_times.count()

    def get_authors_count(self):
        return self.authors.count()

    class Meta:
        ordering = ['-created']
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        db_table = 'recipe'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Recipe, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Recipe, self).delete(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_category', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_category', args=[str(self.id)])

    def get_recipes(self):
        return self.recipes.all()

    def get_recipes_count(self):
        return self.recipes.count()

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Category, self).delete(*args, **kwargs)


class CookingTime(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cooking_time', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_cooking_time', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_cooking_time', args=[str(self.id)])

    def get_recipes(self):
        return self.recipes.all()

    def get_recipes_count(self):
        return self.recipes.count()

    class Meta:
        ordering = ['name']
        verbose_name = 'CookingTime'
        verbose_name_plural = 'CookingTimes'
        db_table = 'cooking_time'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(CookingTime, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(CookingTime, self).delete(*args, **kwargs)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_ingredient', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_ingredient', args=[str(self.id)])

    def get_recipes(self):
        return self.recipes.all()

    def get_recipes_count(self):
        return self.recipes.count()

    class Meta:
        ordering = ['name']
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        db_table = 'ingredient'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Ingredient, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Ingredient, self).delete(*args, **kwargs)


class Instruction(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    order = models.PositiveIntegerField(default=1)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('instruction', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_instruction', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_instruction', args=[str(self.id)])

    class Meta:
        ordering = ['order']
        verbose_name = 'Instruction'
        verbose_name_plural = 'Instructions'
        db_table = 'instruction'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Instruction, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Instruction, self).delete(*args, **kwargs)

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('image', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_image', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_image', args=[str(self.id)])

    class Meta:
        ordering = ['name']
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        db_table = 'image'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Image, self).delete(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_tag', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_tag', args=[str(self.id)])

    def get_recipes(self):
        return self.recipes.all()

    def get_recipes_count(self):
        return self.recipes.count()

    class Meta:
        ordering = ['name']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Tag, self).delete(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comment', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_comment', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_comment', args=[str(self.id)])

    class Meta:
        ordering = ['-created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Comment, self).delete(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True, validators=[validate_slug, validate_unicode_slug])
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('edit_author', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete_author', args=[str(self.id)])

    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        db_table = 'author'
        managed = True
        unique_together = ()
        constraints = []
        indexes = []

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Author, self).delete(*args, **kwargs)






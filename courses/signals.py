import os
import json
from django.db.models.signals import pre_save, post_save, pre_delete
from root.settings import BASE_DIR

from django.dispatch import receiver



from courses.models import Course


@receiver(post_save, sender=Course)
def course_save(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.title} is created!')
        print(kwargs)
    else:
        print('Course Updated')



@receiver(pre_delete, sender=Course)
def course_delete(sender, instance, **kwargs):
    file_path = os.path.join('courses/delete_courses/', f'course_{instance.id}.json')

    course_data = {
        'id': instance.id,
        'title': instance.title,
        'price': instance.price,
        'description': instance.description,
        'image': instance.image,
        'duration': instance.duration,
        'category': instance.category,
        'video': instance.videos.first,
        'rating': instance.rating,
        'number_of_students': instance.number_of_students,
        'teachers': instance.teachers,

    }

    with open(file_path, mode='w') as file_json:
        json.dump(course_data, file_json, indent=4)

    print(f'{instance.title} is deleted')



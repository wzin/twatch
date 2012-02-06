from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.core.urlresolvers import reverse


from models import Hashes

def hashes_list(request):
    """Show all hashes"""
    return object_list(request, 
        queryset=Hashes.objects.all(),
        template_name='hashes/list.html',
        template_object_name='hash'
    )

def hashes_detail(request, id):
    """View hash detail based on hash id"""
 
    return object_detail(request,
        queryset=Hashes.objects.all(),
        object_id=id,
        template_name='hashes/detail.html',
        template_object_name='hash'
    )

def hashes_create(request):
    """Create new hash"""
 
    return create_object(request,
        model=Hashes,
        template_name='hashes/create.html',
        post_save_redirect=reverse("hashes_list")
    ) 

def hashes_update(request, id):
    """Update hash based on id"""
 
    return update_object(request,
        model=Hashes,
        object_id=id,
        template_name='hashes/update.html',
        post_save_redirect=reverse("hashes_list")
    )

def hashes_delete(request, id):
    """Delete a hash based on id"""
 
    return delete_object(request,
        model=Hashes,
        object_id=id,
        template_name='hashes/delete.html',
        post_delete_redirect=reverse("hashes_list")
    ) 

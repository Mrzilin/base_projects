#!/usr/bin/env python
"""
__project_ = 'base_project'
__file_name__ = 'urls.py'
__author__ = 'carl_xiang'
__time__ = '2020/6/11 2:53 PM'
__description__ = 'Please write the functional description here！'
"""
from django.urls import path, include
from rbac.views import user, organization, menu, role, permission
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', user.UserViewSet)
router.register(r'organizations', organization.OrganizationViewSet)
router.register(r'menus', menu.MenuViewSet)
router.register(r'permissions', permission.PermissionViewSet)
router.register(r'roles', role.RoleViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'auth/login/', user.UserAuthView.as_view()),
    path(r'auth/info/', user.UserInfoView.as_view(), name='user_info'),
    path(r'auth/build/menus/', user.UserBuildMenuView.as_view(), name='build_menus'),
    path(r'api/organization/tree/', organization.OrganizationTreeView.as_view(),name='organizations_tree'),
    path(r'api/organization/user/tree/', organization.OrganizationUserTreeView.as_view(), name='organization_user_tree'),
    path(r'api/menu/tree/', menu.MenuTreeView.as_view(), name='menus_tree'),
    path(r'api/permission/tree/', permission.PermissionTreeView.as_view(), name='permissions_tree'),
    path(r'api/user/list/', user.UserListView.as_view(), name='user_list'),
]

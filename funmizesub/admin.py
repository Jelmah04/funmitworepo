from django.contrib import admin
from django.conf import settings
from .models import *

admin.site.register(User)
admin.site.register(UserMembership)
admin.site.register(Membership)
admin.site.register(Customer)
admin.site.register(Transhistory)
admin.site.register(UserWallet)
admin.site.register(PayHistory)
admin.site.register(Contactinfo)
admin.site.register(Networkplan)

# Register your models here.
# class ContactinfoAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name', 'email', 'phone', 'date')
    # list_display_links = ('name',)
    # list_filter = ('name', 'email', 'phone')
    # list_per_page = 20
    # search_fields = ('name', 'email', 'phone')
# 
# 
# class NetworkplanAdmin(admin.ModelAdmin):
    # list_display = ('id', 'network_name', 'is_available')
    # list_display_links = ('network_name',)
    # list_editable = ('is_available',)
    # list_filter = ('id', 'network_name', 'is_available')
    # list_per_page = 10
    # search_fields = ('id', 'network_name', 'is_available')
# 
# 
# class PlanamountAdmin(admin.ModelAdmin):
    # list_display = ('id', 'network_type', 'volume', 'amount', 'is_available')
    # list_display_links = ('network_type',)
    # list_editable = ('is_available',)
    # list_filter = ('id', 'network_type', 'volume', 'amount', 'is_available')
    # list_per_page = 20
    # search_fields = ('id', 'network_type', 'volume', 'amount', 'is_available')
# 
# 
# class AddbalancetouserAdmin(admin.ModelAdmin):
    # list_display = ('id', 'refcode', 'email', 'amount_to_add')
    # list_display_links = ('email','refcode')
    # list_filter = ('id', 'email','refcode', 'amount_to_add')
    # list_per_page = 20
    # search_fields = ('id','refcode', 'email', 'amount_to_add')
# 
# 
# class CustomerAdmin(admin.ModelAdmin):
    # list_display = ('id', 'email', 'status', 'referral_id')
    # list_display_links = ('email',)
    # list_filter = ('id', 'email', 'status', 'referral_id')
    # list_per_page = 20
    # search_fields = ('id', 'email')
# 
# 
# class WalletAdmin(admin.ModelAdmin):
    # list_display = ('id', 'customer', 'new_balance', 'old_balance', 'date')
    # list_display_links = ('new_balance',)
    # list_filter = ('id', 'customer', 'new_balance', 'date')
    # list_per_page = 20
    # search_fields = ('id', 'customer', 'new_balance', 'date')

# class Transaction_HistoryAdmin(admin.ModelAdmin):
    # list_display = ('id', 'user', 'reference_id', 'volume', 'amount', 'status', 'card_number', 'service', 'prebal', 'postbal', 'date')
    # list_display_links = ('card_number', 'reference_id')
    # list_filter = ('id', 'reference_id', 'volume', 'status', 'card_number', 'service', 'date')
    # list_per_page = 20
    # search_fields = ('id', 'reference_id', 'volume', 'status', 'card_number', 'service', 'date')
# 


# admin.site.register(Wallet, WalletAdmin)
# admin.site.register(Planamount, PlanamountAdmin)
# admin.site.register(Addbalancetouser, AddbalancetouserAdmin)
# admin.site.register(CustomUser)

# class UserwalletAdmin(admin.ModelAdmin):
    # list_display = ('id', 'customer', 'current_balance', 'previous_balance', 'date')
    # list_display_links = ('current_balance',)
    # list_filter = ('id', 'customer', 'current_balance', 'date')
    # list_per_page = 20
    # search_fields = ('id', 'customer', 'current_balance', 'date')
# 
# 
# class CustomerprofileAdmin(admin.ModelAdmin):
    # list_display = ('id', 'username', 'email', 'status', 'referral_id')
    # list_display_links = ('username',)
    # list_filter = ('id', 'username', 'status', 'referral_id')
    # list_per_page = 20
    # search_fields = ('id', 'username', 'email')



# admin.site.register(Userwallet, UserwalletAdmin)
# admin.site.register(Customerprofile, CustomerprofileAdmin)
# 
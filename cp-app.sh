copy_app () {
    rm -rf $2
    cp -r $1 $2
    find $2 -type d -name "__pycache__" -exec rm -rf {} +
    find $2 -type f -exec sed -i '' -e "s/$1/$2/g" {} +
}

copy_app "shop" "shop01"
copy_app "shop" "shop02"
copy_app "shop" "shop03"
copy_app "shop" "shop04"
copy_app "shop" "shop05"
copy_app "shop" "shop06"
copy_app "shop" "shop07"
copy_app "shop" "shop08"
copy_app "shop" "shop09"
copy_app "shop" "shop10"
copy_app "shop" "shop11"
copy_app "shop" "shop12"
copy_app "shop" "shop13"
copy_app "shop" "shop14"
copy_app "shop" "shop15"
copy_app "shop" "shop16"
copy_app "shop" "shop17"
copy_app "shop" "shop18"
copy_app "shop" "shop19"
copy_app "shop" "shop20"


# `python manage.py test`
# Creating test database for alias 'default'...
# AVG execution time 22s
# Ran 152 tests in 0.8s to 1.1s
# AVG total execution time 23s


# ➜ `python manage.py squashmigrations shop 0001 0026`
# Will squash the following migrations:
#  - 0001_initial
#  - 0002_customer_is_premium
#  - 0003_shippingaddress
#  - 0004_migrate_shipping_address
#  - 0005_remove_customer_shipping_state
#  - 0006_remove_customer_shipping_province
#  - 0007_remove_customer_shipping_city
#  - 0008_remove_customer_shipping_zip_code
#  - 0009_remove_customer_shipping_address
#  - 0010_remove_customer_shipping_name
#  - 0011_alter_shippingaddress_address_and_more
#  - 0012_order
#  - 0013_order_created_at
#  - 0014_orderline
#  - 0015_alter_customer_user
#  - 0016_customer_customer_type
#  - 0017_migrate_is_premium_to_customer_type
#  - 0018_remove_customer_is_premium
#  - 0019_alter_customer_customer_type
#  - 0020_alter_customer_customer_type
#  - 0021_alter_customer_customer_type
#  - 0022_alter_customer_customer_type
#  - 0023_alter_customer_customer_type
#  - 0024_alter_customer_customer_type
#  - 0025_rename_product_quantity_orderline_quantity
#  - 0026_product
# Do you wish to proceed? [yN] y
# Optimizing...
#   Optimized from 29 operations to 27 operations.
# Created new squashed migration shop/migrations/0001_initial_squashed_0026_product.py
#   You should commit this migration but leave the old ones in place;
#   the new migration will be used for new installs. Once you are sure
#   all instances of the codebase have applied the migrations you squashed,
#   you can delete them.
# Manual porting required
#   Your migrations contained functions that must be manually copied over,
#   as we could not safely copy their implementation.
#   See the comment at the top of the squashed migration for details.
# Squashed migration couldn't be formatted using the "black" command. You can call it manually.


# `python manage.py test`
# Creating test database for alias 'default'...
# AVG execution time 19s
# Ran 152 tests in 0.8s to 1.1s
# AVG total execution time 20s


# `ls -1 shop/migrations | grep -v -e "__init__.py" -e "__pycache__"`

recreate_migrations () {
    ls -1 $1/migrations | grep -v -e "__init__.py" -e "__pycache__"
    rm -rf $1/migrations
    python manage.py makemigrations $1 --name "init_squashed"
    git checkout $1/migrations
}
# recreate_migrations "shop"


# `python manage.py test`
# Creating test database for alias 'default'...
# AVG execution time 8s
# Ran 152 tests in 0.04s to 0.06s
# AVG total execution time 8s



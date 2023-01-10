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

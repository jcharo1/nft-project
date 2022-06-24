from os import walk, rename
import os
path ='layers/clothes'
filenames = next(walk(path), (None, None, []))[2]  # [] if no file
# os.rename("python","python2")


likey_names = [
  {
    "new_name": "inky_darling_clementine.png",
    "old": "tattoo_tan_01.png"
  },
  {
    "new_name": "jittery_jade.png",
    "old": "mint_01.png"
  },
  {
    "new_name": "inky_opera_red.png",
    "old": "tattoo_01.png"
  },
  {
    "new_name": "inky_jittery_jade.png",
    "old": "tattoo_softgreen_01.png"
  },
  {
    "new_name": "korichnewyi_brown.png",
    "old": "lightbrow_01.png"
  },
  {
    "new_name": "inky_blue_dacnis.png",
    "old": "tattoo_skyblue_01.png"
  },
  {
    "new_name": "purplue.png",
    "old": "purple_01.png"
  },
  {
    "new_name": "dimple.png",
    "old": "softpink_01.png"
  },
  {
    "new_name": "inky_dark_sienna.png",
    "old": "tattoo_dark_01.png"
  },
  {
    "new_name": "eastern_spice.png",
    "old": "skin_01.png"
  },
  {
    "new_name": "vivid_cerise.png",
    "old": "darkpink_01.png"
  },
  {
    "new_name": "inky_herbivore.png",
    "old": "tattoo_limeegreen_01.png"
  },
  {
    "new_name": "lavender_magenta.png",
    "old": "pink_01.png"
  },
  {
    "new_name": "inky_dark_periwinkle.png",
    "old": "tattoo_purrrple_01.png"
  },
  {
    "new_name": "inky_trusted_purple.png",
    "old": "tattoo_purplee_01.png"
  },
  {
    "new_name": "sepia_black.png",
    "old": "brown_01.png"
  },
  {
    "new_name": "delightful_dandelion.png",
    "old": "yellow_01.png"
  },
  {
    "new_name": "sparkling_red.png",
    "old": "red_01.png"
  },
  {
    "new_name": "porcelain_rose.png",
    "old": "redish_01.png"
  },
  {
    "new_name": "inky_lago_blue.png",
    "old": "tattoo_teal_01.png"
  },
  {
    "new_name": "inky_rose_cheeks.png",
    "old": "tattoo_softpink_01.png"
  },
  {
    "new_name": "royal_lavender.png",
    "old": "lpurple_01.png"
  },
  {
    "new_name": "rockman_blue.png",
    "old": "blueskin_01.png"
  },
  {
    "new_name": "inky_royal_lavender.png",
    "old": "tattoo_purple_01.png"
  },
  {
    "new_name": "herbivore.png",
    "old": "lightgreen_01.png"
  },
  {
    "new_name": "dark_periwinkle.png",
    "old": "backuplikeytemp4k_01.png"
  },
  {
    "new_name": "date_fruit_brown.png",
    "old": "tan_01.png"
  },
  {
    "new_name": "inky_lingonberry_punch.png",
    "old": "tattoo_softred_01.png"
  },
  {
    "new_name": "lingonberry_punch.png",
    "old": "lred_01.png"
  },
  {
    "new_name": "cinnamon_ice.png",
    "old": "pale_01.png"
  },
  {
    "new_name": "inky_herbivore.png",
    "old": "tattoo_limegreen_01.png"
  },
  {
    "new_name": "spring_wisteria.png",
    "old": "lightpink_01.png"
  },
  {
    "new_name": "blue_dacnis.png",
    "old": "babybl_01.png"
  },
  {
    "new_name": "inky_rockman_blue.png",
    "old": "tattoo_blue_01.png"
  },
  {
    "new_name": "inky_li\u00e1n_h\u00f3ng_lotus_pink.png",
    "old": "tattoo_pink_01.png"
  },
  {
    "new_name": "dark_sienna.png",
    "old": "notatdark_01.png"
  },
  {
    "new_name": "inky_porcelain_rose.png",
    "old": "tattoo_red_01.png"
  },
  {
    "new_name": "herbivore.png",
    "old": "green_01.png"
  },
  {
    "new_name": "water_sports.png",
    "old": "brightblue_01.png"
  }
]

for x in filenames:

   new = x[:len(x)-4] + ">10" + ".png"
   new_name = x.replace(x,new)
   
   os.rename(path + "/" + x ,path + "/" + new_name)

   
# for x in likey_names:
#    print(x["new_name"])



   # new_name = x.replace("-","_")
   # os.rename(path + "/" + x ,path + "/" + new_name)



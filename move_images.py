import os
import shutil

source_dir = r"C:\Users\nizat\.gemini\antigravity\brain\2620ef46-3d1b-4f46-8105-c2fa3f2c308f"
dest_dir = r"d:\havva-store-system\public\images\products"

mapping = {
    "jasmine_rice_boutique_1775107834707.png": "jasmine_rice.png",
    "knife_oil_boutique_1775107851452.png": "knife_oil.png",
    "gula_prai_boutique_1775107870372.png": "gula_prai.png",
    "maggi_noodles_boutique_1775107886211.png": "maggi_noodles.png",
    "lexus_biscuits_boutique_1775107904866.png": "lexus_biscuits.png",
    "mister_potato_boutique_1775107925757.png": "mister_potato.png",
    "nescafe_classic_boutique_1775107942774.png": "nescafe.png",
    "dutch_lady_milk_boutique_1775107960665.png": "dutch_lady.png",
    "sunlight_dishwash_boutique_1775107981449.png": "sunlight.png",
    "dynamo_detergent_boutique_1775107996149.png": "dynamo.png",
    "nano_blue_detergent_boutique_1775108011963.png": "nano_blue.png",
    "nano_floor_cleaner_boutique_1775108030124.png": "nano_floor.png",
    "pantene_shampoo_boutique_1775108049547.png": "pantene.png",
    "dettol_body_wash_boutique_1775108065891.png": "dettol.png",
    "nano_white_cleanser_boutique_1775108080810.png": "nano_white_cleanser.png",
    "nano_white_serum_boutique_1775108099815.png": "nano_white_serum.png"
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for src_name, dest_name in mapping.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_name} to {dest_name}")
    else:
        print(f"Warning: {src_name} not found in {source_dir}")

import pickle
import pprint

with open("/home/slewis/fireprot_dataset/fireprot_upload/csvs/fireprot_splits.pkl", "rb") as pkl:
    old_data = pickle.load(pkl)
    pprint.pprint(old_data)

    new_data = old_data
    new_data["train"].insert(0, "1BX2_DRB15")

    pprint.pprint(new_data)
    with open("/home/slewis/fireprot_dataset/fireprot_upload/csvs/fireprot_splits_EDIT.pkl", "wb") as new_pkl:
        pickle.dump(new_data, new_pkl)
#fireprot_dataset/fireprot_upload/pdbs/MHCs/1BX2_DRB15.pdb

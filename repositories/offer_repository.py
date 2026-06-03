# repositories/offer_repository.py

import json

from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
file_path = DATA_DIR / "offers.json"

def get_all_offers():

    with open(file_path) as f:
        return json.load(f)

def get_offer(offer_id):

    offers = get_all_offers()

    for offer in offers:
        if offer["offerId"] == offer_id:
            return offer

    return None
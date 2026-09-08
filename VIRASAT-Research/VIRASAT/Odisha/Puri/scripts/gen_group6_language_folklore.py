"""
gen_group6_language_folklore.py - Generates Documents 16, 17, and 32.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_16():
    doc = PuriDocBuilder(
        title="Literature & Linguistic Heritage: Classical Odia, Panchasakhas, & Jayadeva",
        doc_number="16",
        category="Literature & Languages"
    )

    doc.add_h1("1. Odia as a Classical Language (Classical Status Dossier 2014)")
    doc.add_paragraph("In February 2014, the Government of India officially accorded Odia the status of the 6th Classical Language of India (joining Sanskrit, Tamil, Telugu, Kannada, and Malayalam). The linguistic dossier established an unbroken literary antiquity exceeding 2,000 years, anchored by the Ashokan rock edicts at Dhauli (3rd c. BCE), the Kharavela Hathigumpha inscription (1st c. BCE), and the 8th-century Charyapada Buddhist mystic poems. In Puri, Odia developed into a profound vehicle for vernacular theology and high poetic literature.")

    headers = ["Literary Era / Text", "Author / Period", "Theological & Cultural Impact in Puri"]
    rows = [
        ["Gita Govinda (ଗୀତଗୋବିନ୍ଦ)", "Kavi Jayadeva (12th Century CE)", "Sanskrit lyric masterpiece celebrating Radha-Krishna divine love; woven into temple ritual fabrics and daily song."],
        ["Odia Mahabharata (ମହାଭାରତ)", "Sarala Das (15th Century CE)", "The foundational vernacular epic of Odisha; localized puranic episodes into Odia cultural reality."],
        ["Jagamohana / Dandi Ramayana", "Balarama Das (Panchasakha - 16th c.)", "Pioneered egalitarian Bhakti; first literary documentation of Rasagola offered to Lakshmi."],
        ["Odia Bhagavata (ଭାଗବତ)", "Atibadi Jagannatha Das (16th c.)", "The definitive spiritual text of Odisha; placed in village Bhagavata Tungis; praised by Chaitanya Mahaprabhu."],
        ["Panchasakha Mystic Texts", "Achyutananda, Jasovanta, Ananta Das", "Sunya Vada (Void philosophy), esoteric Tantric Vaishnavism, and prophecy texts (Malika)."]
    ]
    doc.add_table(headers, rows, [1.5, 1.8, 3.2])

    doc.add_h1("2. Tourist Linguistic Guide: Essential Odia for Cultural Visitors")
    doc.add_paragraph("A practical linguistic reference for pilgrims and heritage visitors to Puri:")
    headers = ["English Phrase", "Odia Script", "Transliteration", "Cultural Usage / Context"]
    rows = [
        ["Greetings / Welcome", "ନମସ୍କାର / ଜୟ ଜଗନ୍ନାଥ", "Namaskar / Jai Jagannath", "Universal greeting in Puri; invokes Lord Jagannath."],
        ["Thank you", "ଧନ୍ୟବାଦ", "Dhanyabad", "Polite formal expression of gratitude."],
        ["Where is the temple?", "ମନ୍ଦିର କେଉଁଠି?", "Mandira keunthi?", "Asking directions to a sacred shrine."],
        ["How much is this?", "ୟାର ଦାମ୍ କେତେ?", "Yara daam kete?", "Inquiring about prices in markets or craft villages."],
        ["Give me Mahaprasad", "ମୋତେ ମହାପ୍ରସାଦ ଦିଅନ୍ତୁ", "Mote Mahaprasad diyantu", "Requesting sacred food at Anand Bazaar."],
        ["Water / Drinking water", "ପାଣି / ପିଇବା ପାଣି", "Pani / Piiba pani", "Essential utility inquiry."],
        ["Very beautiful", "ବହୁତ ସୁନ୍ଦର", "Bahut sundar", "Appreciating Pattachitra painting or temple art."],
        ["Goodbye / See you", "ଆସୁଛି / ପରେ ଦେଖାହେବା", "Aasuchi / Pare dekha heba", "Polite farewell phrase ('I will return')."]
    ]
    doc.add_table(headers, rows, [1.4, 1.4, 1.5, 2.2])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S012"),
        get_source("PUR-S018"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "16_Literature_and_Languages.docx"))

def generate_doc_17():
    doc = PuriDocBuilder(
        title="Folklore, Myths, & Sacred Legends of Puri (Katha & Mahatmya)",
        doc_number="17",
        category="Folklore & Mythological Lore"
    )

    doc.add_h1("1. The Legendary Origin of Jagannath (Indradyumna Mahatmya)")
    doc.add_paragraph("Narrated in the Skanda Purana and Brahma Purana, the legendary origin recounts King Indradyumna of Avanti, who dispatched his Brahmin priest Vidyapati to locate the supreme form of Vishnu (Nilamadhava). Guided to the deep forests of Nilachala, Vidyapati discovered that the tribal Sabara chieftain Viswavasu worshipped Nilamadhava in absolute secrecy in a hidden cave:")
    doc.add_bullet("The Mustard Seed Trail: Blindfolded by Viswavasu, Vidyapati secretly dropped mustard seeds along the path, which sprouted during the monsoons, allowing him to relocate the cave.", "[MYTHOLOGICAL MOTIF] ")
    doc.add_bullet("Disappearance of Nilamadhava & The Floating Log: Nilamadhava vanished, commanding Indradyumna in a dream to construct a temple and await a miraculous divine log (Daru) floating ashore at Banki Muhana (Puri beach).", "[SACRED LEGEND] ")
    doc.add_bullet("Ananta Maharana (Viswakarma in Disguise): The divine architect arrived as an old carpenter, agreeing to carve the deities inside the locked temple under the condition that no one open the doors for 21 days. Overcome by anxiety, Queen Gundicha persuaded the king to unlock the doors after 14 days of silence, finding three unfinished forms with large, round eyes and armless stumps.", "[FOLKLORIC NARRATIVE] ")

    doc.add_h1("2. The Kanchi-Kaveri Expedition & Gopa-Gopala (Bada Danda Legend)")
    doc.add_paragraph("One of Odisha's most cherished patriotic and romantic legends centers on Gajapati Purushottama Deva (15th century). When the King of Kanchi insulted the Gajapati for performing the sweeper's duty (Chhera Pahara) during Rath Yatra and refused to give his daughter Princess Padmavati in marriage, Purushottama Deva marched his army south. Tradition holds that Lord Jagannath and Lord Balabhadra rode ahead of the royal army on a black and a white horse. Parched from riding, they bought sweet curd (Dahi) from a milkmaid named Manika on the banks of Chilika Lake, handing over a jewel-encrusted signet ring as payment. The spot was christened Manikapatana, and the victorious Gajapati brought Princess Padmavati to Puri, wedded to her as he performed Chhera Pahara.")

    doc.add_sources_section([
        get_source("PUR-S008"),
        get_source("PUR-S009"),
        get_source("PUR-S018"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "17_Folklore_Myths_and_Legends.docx"))

def generate_doc_32():
    doc = PuriDocBuilder(
        title="Folklore & Story Database: Structured Register of Oral & Sacred Narratives",
        doc_number="32",
        category="Folklore & Narrative Database"
    )

    doc.add_h1("1. Master Index of Puri Myths, Legends, & Oral Traditions")
    headers = ["Story ID", "Title / Narrative Name", "Classification Tag", "Central Characters", "Primary Motif / Sacred Lesson", "Associated Site in Puri"]
    rows = [
        ["STORY-001", "The Indradyumna & Gundicha Legend", "Sacred Origin Myth", "Indradyumna, Gundicha, Viswakarma", "Unfinished divine form; cosmic will supersedes human impatience.", "Gundicha Temple / Nilachala"],
        ["STORY-002", "Viswavasu & Vidyapati (Nilamadhava)", "Tribal-Brahmanic Legend", "Viswavasu (Sabara), Vidyapati", "Synthesis of indigenous forest worship with classical Vedic worship.", "Koili Baikuntha / Banki Muhana"],
        ["STORY-003", "Kanchi-Kaveri & Manika Gauduni", "Historical-Devotional Folk Epic", "Purushottama Deva, Manika, Horse Deities", "Divine solidarity with the royal servitor; validation of Chhera Pahara.", "Manikapatana / Bada Danda"],
        ["STORY-004", "Bhakta Salabega & the Halting Chariot", "Devotional Bhakti Legend", "Salabega (Muslim devotee), Jagannath", "Divine love transcends religious, racial, and caste boundaries.", "Salabega Samadhi / Grand Road"],
        ["STORY-005", "Dasia Bauri's Coconut Offering", "Egalitarian Caste Lore", "Dasia Bauri (Outcaste weaver), Jagannath", "Deity's hand emerges directly from the temple to accept sincere offering.", "Balighai / Singhadwara"],
        ["STORY-006", "Bandhu Mohanty & the Golden Plate", "Miracle / Devotional Tale", "Bandhu Mohanty, Jagannath, Lakshmi", "Compassion of Jagannath feeding a destitute devotee during famine.", "Jagannath Temple Inner Sanctum"],
        ["STORY-007", "The Legend of Kakabhusundi (Rohini Kunda)", "Puranic Animal Myth", "Crow Kakabhusundi, Lord Vishnu", "Sacred waters of Rohini Kunda grant instantaneous liberation.", "Rohini Kunda (Inner Courtyard)"],
        ["STORY-008", "Garmata Mahavir & Ocean Boundary", "Guardian Deity Legend", "Lord Hanuman (Bedi Mahavir), Samudra", "Hanuman tied with golden chains to prevent the ocean from drowning Puri.", "Bedi Mahavir Temple (Sea Beach)"]
    ]
    doc.add_table(headers, rows, [0.8, 1.4, 1.2, 1.2, 1.2, 0.7])

    doc.add_sources_section([
        get_source("PUR-S008"),
        get_source("PUR-S009"),
        get_source("PUR-S018"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "32_Folklore_and_Story_Database.docx"))

if __name__ == "__main__":
    generate_doc_16()
    generate_doc_17()
    generate_doc_32()
    print("Group 6 completed successfully.")

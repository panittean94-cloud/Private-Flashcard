import os
from PIL import Image

pages_dir = r"c:\Users\thana\Desktop\Private-Flashcard\images\pages"
out_dir = r"c:\Users\thana\Desktop\Private-Flashcard\images\diagrams"
os.makedirs(out_dir, exist_ok=True)

crops = [
    # Exam papers (1275 x 1165)
    ("exam_p28_right_hand.png", "fune_p28.png", (40, 100, 1235, 550)),
    ("exam_p29_ammeter_cdrx.png", "fune_p29.png", (40, 200, 1235, 1050)),
    ("exam_p30_wattmeter.png", "fune_p30.png", (40, 480, 1235, 1080)),
    ("exam_p32_transformer_core.png", "fune_p32.png", (40, 220, 1235, 650)),
    
    # Review & Lecture notes (1275 x 1756 or 1165)
    ("dc_motor_circuit.png", "fune_p03.png", (50, 420, 1225, 1100)),
    ("dc_generator_circuit.png", "fune_p04.png", (50, 420, 1225, 1100)),
    ("dc_shunt_speed_control.png", "fune_p05.png", (50, 200, 1225, 880)),
    ("transformer_audio_matching.png", "fune_p07.png", (50, 280, 1225, 1000)),
    ("transformer_equivalent_circuit.png", "fune_p10.png", (50, 120, 1225, 850)),
    ("power_system_stages.png", "fune_p13.png", (50, 280, 1225, 950)),
    ("transmission_towers.png", "fune_p14.png", (50, 250, 1225, 1200)),
    ("ammeter_voltmeter_basic.png", "fune_p16.png", (50, 200, 1225, 1150)),
    ("ohmmeter_circuits.png", "fune_p17.png", (50, 180, 1225, 1150)),
    ("multirange_ammeter.png", "fune_p18.png", (50, 150, 1225, 1100)),
    ("multirange_voltmeter.png", "fune_p20.png", (50, 150, 1225, 1000)),
    ("diode_circuits.png", "fune_p22.png", (50, 180, 1225, 1050)),
    ("transistor_bjt_mosfet.png", "fune_p23.png", (50, 180, 1225, 1150)),
]

for out_name, src_name, bbox in crops:
    src_path = os.path.join(pages_dir, src_name)
    if os.path.exists(src_path):
        im = Image.open(src_path)
        cropped = im.crop(bbox)
        # remove excess white border if needed
        out_path = os.path.join(out_dir, out_name)
        cropped.save(out_path)
        print(f"Saved: {out_name} size={cropped.size}")
    else:
        print(f"Source not found: {src_name}")

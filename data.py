MODEL_FEATURES = ["nitrogen", "phosphorus", "potassium", "temperature", "humidity", "ph", "rainfall"]


MODEL_CROP_PROFILES = {
    "Rice": {"n": (70, 120), "p": (35, 60), "k": (35, 55), "temp": (22, 32), "humidity": (70, 90), "ph": (5.5, 7.0), "rainfall": (150, 300), "yield": 3.8},
    "Wheat": {"n": (50, 100), "p": (35, 60), "k": (20, 45), "temp": (15, 25), "humidity": (45, 70), "ph": (6.0, 7.8), "rainfall": (50, 120), "yield": 3.4},
    "Maize": {"n": (60, 110), "p": (35, 70), "k": (30, 60), "temp": (20, 32), "humidity": (50, 75), "ph": (5.8, 7.5), "rainfall": (60, 140), "yield": 4.5},
    "Cotton": {"n": (60, 100), "p": (25, 55), "k": (40, 80), "temp": (24, 35), "humidity": (45, 70), "ph": (6.0, 8.0), "rainfall": (50, 110), "yield": 2.2},
    "Sugarcane": {"n": (100, 160), "p": (40, 80), "k": (80, 140), "temp": (22, 34), "humidity": (60, 85), "ph": (6.0, 7.8), "rainfall": (120, 250), "yield": 75.0},
    "Groundnut": {"n": (20, 50), "p": (35, 70), "k": (25, 55), "temp": (24, 32), "humidity": (50, 70), "ph": (6.0, 7.5), "rainfall": (50, 120), "yield": 2.0},
    "Soybean": {"n": (20, 60), "p": (40, 75), "k": (25, 60), "temp": (20, 30), "humidity": (55, 80), "ph": (6.0, 7.5), "rainfall": (60, 140), "yield": 2.5},
    "Mustard": {"n": (40, 80), "p": (25, 55), "k": (15, 40), "temp": (12, 25), "humidity": (40, 65), "ph": (6.0, 8.0), "rainfall": (30, 90), "yield": 1.6},
    "Chickpea": {"n": (20, 50), "p": (30, 60), "k": (20, 45), "temp": (18, 30), "humidity": (35, 60), "ph": (6.0, 8.0), "rainfall": (40, 90), "yield": 1.4},
    "Pigeon Pea": {"n": (20, 55), "p": (35, 65), "k": (20, 50), "temp": (22, 34), "humidity": (45, 70), "ph": (6.0, 7.8), "rainfall": (60, 130), "yield": 1.5},
    "Potato": {"n": (80, 140), "p": (50, 90), "k": (80, 150), "temp": (15, 25), "humidity": (60, 85), "ph": (5.0, 6.8), "rainfall": (50, 110), "yield": 24.0},
    "Tomato": {"n": (60, 110), "p": (45, 80), "k": (60, 120), "temp": (18, 30), "humidity": (55, 80), "ph": (6.0, 7.5), "rainfall": (50, 120), "yield": 28.0},
    "Onion": {"n": (60, 120), "p": (40, 80), "k": (50, 100), "temp": (13, 30), "humidity": (50, 75), "ph": (6.0, 7.5), "rainfall": (40, 100), "yield": 18.0},
    "Banana": {"n": (100, 180), "p": (50, 90), "k": (120, 220), "temp": (24, 34), "humidity": (65, 90), "ph": (6.0, 7.5), "rainfall": (120, 260), "yield": 35.0},
    "Mango": {"n": (40, 90), "p": (20, 50), "k": (40, 90), "temp": (24, 36), "humidity": (45, 75), "ph": (5.5, 7.5), "rainfall": (70, 180), "yield": 8.0},
    "Millets": {"n": (25, 60), "p": (20, 45), "k": (15, 40), "temp": (25, 35), "humidity": (30, 60), "ph": (5.5, 7.5), "rainfall": (25, 80), "yield": 1.8},
    "Barley": {"n": (35, 75), "p": (25, 50), "k": (15, 35), "temp": (12, 24), "humidity": (40, 65), "ph": (6.0, 8.0), "rainfall": (30, 80), "yield": 2.8},
    "Jute": {"n": (60, 110), "p": (30, 60), "k": (35, 70), "temp": (24, 34), "humidity": (70, 90), "ph": (6.0, 7.8), "rainfall": (140, 260), "yield": 2.6},
    "Tea": {"n": (70, 130), "p": (20, 50), "k": (40, 80), "temp": (18, 30), "humidity": (70, 95), "ph": (4.5, 6.0), "rainfall": (150, 300), "yield": 2.1},
    "Coffee": {"n": (60, 120), "p": (25, 55), "k": (45, 90), "temp": (18, 28), "humidity": (60, 85), "ph": (5.0, 6.8), "rainfall": (120, 240), "yield": 1.2},
}


CROP_INFO = {
    "Rice": {"price": 32, "demand": "Very high", "season": "Kharif", "image": "https://images.unsplash.com/photo-1536058810607-3dc7a3b717c1?auto=format&fit=crop&w=700&q=80", "tips": "Needs standing water in early growth. Keep weeds controlled and maintain good drainage near harvest."},
    "Wheat": {"price": 28, "demand": "Very high", "season": "Rabi", "image": "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=700&q=80", "tips": "Best in cool, dry weather. Irrigate at crown root, flowering, and grain filling stages."},
    "Maize": {"price": 24, "demand": "High", "season": "Kharif/Rabi", "image": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=700&q=80", "tips": "Use well-drained soil and avoid waterlogging. Nitrogen split doses improve cob size."},
    "Cotton": {"price": 70, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1594179047519-f347310d3322?auto=format&fit=crop&w=700&q=80", "tips": "Requires warm climate and pest monitoring. Avoid excess irrigation during boll formation."},
    "Sugarcane": {"price": 4, "demand": "Very high", "season": "Annual", "image": "https://images.unsplash.com/photo-1599407384144-7f098bcd29a5?auto=format&fit=crop&w=700&q=80", "tips": "Heavy feeder crop. Apply organic matter and keep steady moisture for better cane weight."},
    "Groundnut": {"price": 75, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1648132539222-466a9e2940f4?auto=format&fit=crop&w=700&q=80", "tips": "Loose sandy loam helps pod development. Avoid waterlogging and add gypsum where needed."},
    "Soybean": {"price": 45, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=700&q=80", "tips": "Use seed treatment and maintain row spacing. It benefits from good drainage."},
    "Mustard": {"price": 62, "demand": "High", "season": "Rabi", "image": "https://images.unsplash.com/photo-1511735643442-503bb3bd348a?auto=format&fit=crop&w=700&q=80", "tips": "Needs cool weather and moderate irrigation. Avoid late sowing to reduce aphid pressure."},
    "Chickpea": {"price": 68, "demand": "High", "season": "Rabi", "image": "https://images.unsplash.com/photo-1612257999756-93f3215aa0e1?auto=format&fit=crop&w=700&q=80", "tips": "Good for low water areas. Avoid excessive irrigation and use disease-free seed."},
    "Pigeon Pea": {"price": 95, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1660644824686-7b01c966ecb0?auto=format&fit=crop&w=700&q=80", "tips": "Deep rooted crop. Grow on well-drained soil and control pod borer early."},
    "Potato": {"price": 22, "demand": "Very high", "season": "Rabi", "image": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=700&q=80", "tips": "Needs loose soil and cool weather. Earthing up protects tubers and improves yield."},
    "Tomato": {"price": 35, "demand": "High", "season": "All season", "image": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=700&q=80", "tips": "Use staking and regular picking. Keep soil moisture even to reduce fruit cracking."},
    "Onion": {"price": 30, "demand": "Very high", "season": "Rabi/Kharif", "image": "https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?auto=format&fit=crop&w=700&q=80", "tips": "Needs nursery care and well-drained beds. Stop irrigation before harvesting mature bulbs."},
    "Banana": {"price": 25, "demand": "High", "season": "Annual", "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=700&q=80", "tips": "Requires rich soil and regular water. Remove suckers except the selected follower."},
    "Mango": {"price": 70, "demand": "High", "season": "Summer", "image": "https://images.unsplash.com/photo-1601493700631-2b16ec4b4716?auto=format&fit=crop&w=700&q=80", "tips": "Needs dry weather during flowering. Prune lightly and manage fruit fly with traps."},
    "Millets": {"price": 38, "demand": "Growing", "season": "Kharif", "image": "https://images.unsplash.com/photo-1603271889486-cf7d33a57a45?auto=format&fit=crop&w=700&q=80", "tips": "Very suitable for dry lands. Avoid too much nitrogen and harvest when grains harden."},
    "Barley": {"price": 27, "demand": "Medium", "season": "Rabi", "image": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=700&q=80", "tips": "Tolerates salinity better than wheat. Best for cool and dry growing periods."},
    "Jute": {"price": 55, "demand": "Medium", "season": "Kharif", "image": "https://images.unsplash.com/photo-1595941069915-4ebc5197c14a?auto=format&fit=crop&w=700&q=80", "tips": "Needs warm humid climate and good rainfall. Retting quality affects fibre price."},
    "Tea": {"price": 180, "demand": "High", "season": "Perennial", "image": "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?auto=format&fit=crop&w=700&q=80", "tips": "Prefers acidic soil and high humidity. Regular pruning keeps bushes productive."},
    "Coffee": {"price": 250, "demand": "High", "season": "Perennial", "image": "https://images.unsplash.com/photo-1447933601403-0c6688de566e?auto=format&fit=crop&w=700&q=80", "tips": "Grows well under shade. Maintain mulch and protect from berry borer."},
    "Coconut": {"price": 35, "demand": "High", "season": "Perennial", "image": "https://images.unsplash.com/photo-1580984969071-a8da5656c2fb?auto=format&fit=crop&w=700&q=80", "tips": "Needs coastal or humid climate. Provide basin irrigation in dry months."},
    "Turmeric": {"price": 95, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1615485500704-8e990f9900f7?auto=format&fit=crop&w=700&q=80", "tips": "Use healthy rhizomes and mulch after planting. Harvest when leaves turn yellow."},
    "Ginger": {"price": 110, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1603431776792-6f9ba4b8ddee?auto=format&fit=crop&w=700&q=80", "tips": "Needs partial shade and loose soil. Avoid water stagnation to prevent rhizome rot."},
    "Cabbage": {"price": 18, "demand": "Medium", "season": "Rabi", "image": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?auto=format&fit=crop&w=700&q=80", "tips": "Cool climate crop. Regular irrigation and spacing help firm head formation."},
    "Cauliflower": {"price": 30, "demand": "High", "season": "Rabi", "image": "https://images.unsplash.com/photo-1584615467033-75627d04dffe?auto=format&fit=crop&w=700&q=80", "tips": "Needs cool temperatures. Protect curds from sun exposure for better quality."},
    "Brinjal": {"price": 28, "demand": "Medium", "season": "All season", "image": "https://images.unsplash.com/photo-1605197376324-7b0b2f1991ab?auto=format&fit=crop&w=700&q=80", "tips": "Pick fruits at tender stage. Monitor shoot and fruit borer regularly."},
    "Okra": {"price": 40, "demand": "High", "season": "Kharif/Summer", "image": "https://images.unsplash.com/photo-1425543103986-22abb7d7e8d2?auto=format&fit=crop&w=700&q=80", "tips": "Warm season vegetable. Frequent picking improves total production."},
    "Green Gram": {"price": 95, "demand": "High", "season": "Kharif/Summer", "image": "https://images.unsplash.com/photo-1615485925763-86786288908a?auto=format&fit=crop&w=700&q=80", "tips": "Short duration pulse. Use seed treatment and avoid waterlogging."},
    "Black Gram": {"price": 100, "demand": "High", "season": "Kharif", "image": "https://images.unsplash.com/photo-1607349913338-fca6f7fc42d0?auto=format&fit=crop&w=700&q=80", "tips": "Suitable for rainfed farming. Timely weed control is important in early growth."},
    "Lentil": {"price": 82, "demand": "Medium", "season": "Rabi", "image": "https://images.unsplash.com/photo-1597714026720-8f74c62310ba?auto=format&fit=crop&w=700&q=80", "tips": "Grows in cool dry weather. Avoid heavy irrigation and improve drainage."},
    "Pea": {"price": 45, "demand": "Medium", "season": "Rabi", "image": "https://images.unsplash.com/photo-1587486913049-53fc88980cfc?auto=format&fit=crop&w=700&q=80", "tips": "Needs cool weather. Support climbing varieties and pick pods regularly."},
    "Sesame": {"price": 130, "demand": "Medium", "season": "Kharif", "image": "https://images.unsplash.com/photo-1508747703725-719777637510?auto=format&fit=crop&w=700&q=80", "tips": "Drought tolerant oilseed. Avoid waterlogging and harvest before capsule shattering."},
    "Sunflower": {"price": 55, "demand": "Medium", "season": "Rabi/Summer", "image": "https://images.unsplash.com/photo-1470509037663-253afd7f0f51?auto=format&fit=crop&w=700&q=80", "tips": "Needs full sunlight. Pollination improves when bee activity is good."},
    "Papaya": {"price": 28, "demand": "Medium", "season": "Perennial", "image": "https://images.unsplash.com/photo-1617112848923-cc2234396a8d?auto=format&fit=crop&w=700&q=80", "tips": "Needs well-drained soil. Remove diseased plants quickly to reduce virus spread."},
    "Grapes": {"price": 85, "demand": "High", "season": "Perennial", "image": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=700&q=80", "tips": "Requires training and pruning. Manage powdery mildew and irrigation carefully."},
}


def get_crop_info_list():
    return [{"name": name, **details} for name, details in CROP_INFO.items()]

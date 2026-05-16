import random
import sys

class ElitePromptEngine:
    def __init__(self):
        # 依據 AI 算圖高頻數據，精選 15 項最常見且效果卓越的元素矩陣
        self.matrix = {
            "Who": {
                "name": "誰 (Who)",
                "options": {
                    "1": {"ch": "男人", "en": "A sophisticated man"},
                    "2": {"ch": "女人", "en": "A sophisticated woman"},
                    "3": {"ch": "男孩", "en": "A cheerful boy"},
                    "4": {"ch": "女孩", "en": "A graceful girl"},
                    "5": {"ch": "高階商務男士", "en": "An elite businessman"},
                    "6": {"ch": "高階商務女士", "en": "An elite businesswoman"},
                    "7": {"ch": "創新創業家", "en": "A visionary entrepreneur"},
                    "8": {"ch": "資深產業導師", "en": "An experienced senior mentor"},
                    "9": {"ch": "頂級建築設計師", "en": "A professional architect"},
                    "10": {"ch": "AI 科技工程師", "en": "A cutting-edge tech engineer"},
                    "11": {"ch": "國際時尚模特", "en": "A high-fashion runway model"},
                    "12": {"ch": "卓越企業領導者", "en": "A charismatic corporate leader"},
                    "13": {"ch": "專業資產顧問", "en": "An expert financial consultant"},
                    "14": {"ch": "高淨值投資人", "en": "A high-net-worth investor"},
                    "15": {"ch": "工藝職人", "en": "A dedicated master craftsman"}
                }
            },
            "Look": {
                "name": "長相神態 (Look)",
                "options": {
                    "1": {"ch": "精明幹練", "en": "sharp and professional look"},
                    "2": {"ch": "溫和微笑", "en": "with a warm and confident smile"},
                    "3": {"ch": "專注沉穩", "en": "with a focused and calm expression"},
                    "4": {"ch": "具備前瞻遠見", "en": "with a visionary and ambitious gaze"},
                    "5": {"ch": "優雅高貴", "en": "with an elegant and sophisticated appearance"},
                    "6": {"ch": "朝氣蓬勃", "en": "full of energy and enthusiasm"},
                    "7": {"ch": "睿智深思", "en": "with a wise and thoughtful demeanor"},
                    "8": {"ch": "堅毅果斷", "en": "showing a determined and resilient attitude"},
                    "9": {"ch": "時尚潮流", "en": "with a trendy and stylish aesthetic"},
                    "10": {"ch": "親切隨和", "en": "with an approachable and friendly vibe"},
                    "11": {"ch": "嚴謹理性", "en": "with a rigorous and analytical mindset"},
                    "12": {"ch": "熱情洋溢", "en": "radiating deep passion and charisma"},
                    "13": {"ch": "從容淡定", "en": "composing a relaxed and serene presence"},
                    "14": {"ch": "自帶強大氣場", "en": "exuding a powerful and magnetic charisma"},
                    "15": {"ch": "文藝獨特", "en": "with an artistic and uniquely expressive style"}
                }
            },
            "Wear": {
                "name": "服裝 (Wear)",
                "options": {
                    "1": {"ch": "量身正裝西服", "en": "wearing a perfectly tailored luxury suit"},
                    "2": {"ch": "俐落商務套裝", "en": "wearing a sleek, modern corporate blazer"},
                    "3": {"ch": "質商務休閒服", "en": "wearing an upscale smart-casual outfit"},
                    "4": {"ch": "極簡質感運動風", "en": "wearing premium minimalist sportswear"},
                    "5": {"ch": "極簡亞麻襯衫", "en": "wearing a crisp, high-end linen shirt"},
                    "6": {"ch": "高奢晚禮服", "en": "wearing a magnificent luxury evening gown"},
                    "7": {"ch": "經典英倫風衣", "en": "wearing a timeless classic trench coat"},
                    "8": {"ch": "高科技智能服飾", "en": "wearing futuristic tech-wear apparel"},
                    "9": {"ch": "復古丹寧夾克", "en": "wearing a stylish vintage denim jacket"},
                    "10": {"ch": "頂級羊絨毛衣", "en": "wearing an elegant soft cashmere sweater"},
                    "11": {"ch": "專業職人制服", "en": "wearing an authentic artisanal uniform"},
                    "12": {"ch": "帥氣不羈皮夾克", "en": "wearing a premium rugged leather jacket"},
                    "13": {"ch": "波西米亞風服飾", "en": "wearing a flowing bohemian chic dress"},
                    "14": {"ch": "東方傳統正裝", "en": "wearing an elegant traditional oriental attire"},
                    "15": {"ch": "都市高街潮流服裝", "en": "wearing a cutting-edge urban streetwear outfit"}
                }
            },
            "Action": {
                "name": "動作 (Action)",
                "options": {
                    "1": {"ch": "正在發表精彩簡報", "en": "delivering an inspiring keynote presentation"},
                    "2": {"ch": "輕鬆品嚐頂級咖啡", "en": "enjoying a cup of specialty coffee thoughtfully"},
                    "3": {"ch": "專注地分析筆電數據", "en": "analyzing strategic data closely on a laptop screen"},
                    "4": {"ch": "自信從容望向遠方", "en": "looking into the distance with a visionary mindset"},
                    "5": {"ch": "與合作夥伴親切握手", "en": "shaking hands warmly with a business partner"},
                    "6": {"ch": "主持高階策略會議", "en": "leading an executive strategic boardroom discussion"},
                    "7": {"ch": "正式簽署戰略合約", "en": "signing an important international strategic contract"},
                    "8": {"ch": "邁著自信步伐前行", "en": "walking forward with a powerful, confident stride"},
                    "9": {"ch": "與核心團隊輕鬆交談", "en": "laughing and interacting genuinely with teammates"},
                    "10": {"ch": "在白板上繪製發展藍圖", "en": "sketching a corporate blueprint on a whiteboard"},
                    "11": {"ch": "手持麥克風在舞台發言", "en": "speaking eloquently into a microphone on stage"},
                    "12": {"ch": "審視最新的財務圖表", "en": "reviewing complex financial growth charts meticulously"},
                    "13": {"ch": "閉目沉思構想新專案", "en": "deep in creative meditation for a major project"},
                    "14": {"ch": "手勢精準地指向未來螢幕", "en": "gesturing precisely toward a futuristic digital screen"},
                    "15": {"ch": "舉起香檳杯慶祝成功", "en": "toasting a glass of fine champagne to celebrate success"}
                }
            },
            "Where": {
                "name": "哪裡 (Where)",
                "options": {
                    "1": {"ch": "現代高階商務辦公室", "en": "inside a high-end modern corporate headquarters office"},
                    "2": {"ch": "頂樓景觀咖啡廳", "en": "at a luxury rooftop cafe overlooking the city skyline"},
                    "3": {"ch": "充滿陽光的共享空間", "en": "in a sunlit, eco-friendly premium coworking space"},
                    "4": {"ch": "未來感科技展覽廳", "en": "in a futuristic tech convention center"},
                    "5": {"ch": "奢華五星級酒店大堂", "en": "inside the majestic lobby of a 5-star luxury hotel"},
                    "6": {"ch": "陸家嘴金融中心街景", "en": "at the bustling heart of an international financial center"},
                    "7": {"ch": "大器高雅的私人書房", "en": "in a prestigious private library with floor-to-ceiling books"},
                    "8": {"ch": "繁華絢麗的都市街頭", "en": "on a vibrant, upscale metropolitan street at night"},
                    "9": {"ch": "靜謐和諧的溫室植物園", "en": "inside a peaceful, lush botanical greenhouse"},
                    "10": {"ch": "工業風挑高藝術工作室", "en": "in a spacious industrial loft art studio"},
                    "11": {"ch": "高端不動產尊榮沙龍", "en": "inside a premium real estate investment salon"},
                    "12": {"ch": "機場尊榮貴賓候機室", "en": "resting in an exclusive airport VIP lounge"},
                    "13": {"ch": "海景第一排無邊際露台", "en": "on a breathtaking oceanfront terrace next to infinity pool"},
                    "14": {"ch": "極簡主義當代藝術畫廊", "en": "surrounded by fine art in a minimalist gallery"},
                    "15": {"ch": "頂級智能家居客廳", "en": "inside a luxurious, high-tech smart home living room"}
                }
            },
            "Light": {
                "name": "光線 (Light)",
                "options": {
                    "1": {"ch": "高級自然側光", "en": "refined natural side lighting"},
                    "2": {"ch": "溫慢黃金逆光", "en": "golden hour warm backlighting with soft sun flares"},
                    "3": {"ch": "戲劇化明暗對比光", "en": "dramatic chiaroscuro lighting for deep artistic contrast"},
                    "4": {"ch": "柔和商務棚拍高級光", "en": "soft commercial studio portrait lighting"},
                    "5": {"ch": "霓虹電影感氛圍光", "en": "vibrant neon cinematic lighting"},
                    "6": {"ch": "清晨明亮穿透晨光", "en": "bright morning sunlight streaming through windows"},
                    "7": {"ch": "魔幻時刻迷人暮光", "en": "atmospheric moody twilight lighting"},
                    "8": {"ch": "乾淨透亮的高調光", "en": "clean, crisp high-key lighting"},
                    "9": {"ch": "細緻奢華的輪廓光", "en": "sophisticated rim lighting highlighting the silhouette"},
                    "10": {"ch": "陰天柔和漫射光", "en": "soft diffused moody daylight"},
                    "11": {"ch": "賽博朋克藍紫全息光", "en": "cyberpunk holographic glow with blue and purple tones"},
                    "12": {"ch": "溫馨沉靜的燭光感", "en": "warm, intimate candlelit ambiance"},
                    "13": {"ch": "現代建築線條嵌入光", "en": "architectural linear LED lighting"},
                    "14": {"ch": "夢幻耀光斑斕強光", "en": "dramatic lens flare with anamorphic streaks"},
                    "15": {"ch": "神聖壯麗的耶穌光", "en": "volumetric god rays breaking through the background"}
                }
            },
            "Style": {
                "name": "風格 (Style)",
                "options": {
                    "1": {"ch": "極致寫實攝影", "en": "Hyper-realistic commercial photography"},
                    "2": {"ch": "富比士雜誌封面風", "en": "Modern Forbes business magazine cover style"},
                    "3": {"ch": "好萊塢電影感大片", "en": "Cinematic masterpiece, award-winning cinematography"},
                    "4": {"ch": "3D Octane 頂級渲染藝術", "en": "8k resolution, ultra-detailed 3D octane render art"},
                    "5": {"ch": "極簡時尚雜誌大牌風", "en": "Minimalist editorial fashion magazine style"},
                    "6": {"ch": "賽博朋克未來主義", "en": "Cyberpunk futurism aesthetic"},
                    "7": {"ch": "溫暖復古經典膠卷風", "en": "Warm retro vintage film photography style"},
                    "8": {"ch": "建築摘要空間雜誌風", "en": "Architectural Digest interior lifestyle style"},
                    "9": {"ch": "當代印象派油畫風", "en": "Impressionistic fine art oil painting style"},
                    "10": {"ch": "現代科技數位插畫", "en": "Modern clean digital illustration"},
                    "11": {"ch": "黑白經典藝術攝影", "en": "Fine art black and white photography"},
                    "12": {"ch": "波普藝術鮮豔插畫", "en": "Bold pop art vector illustration"},
                    "13": {"ch": "新東方美學現代融合", "en": "Modern oriental fusion aesthetic style"},
                    "14": {"ch": "通透水彩柔和渲染", "en": "Translucent watercolor wash style"},
                    "15": {"ch": "超現實主義夢境大片", "en": "Surrealist dreamscape artistic style"}
                }
            },
            "Camera": {
                "name": "鏡頭 (Camera)",
                "options": {
                    "1": {"ch": "特寫鏡頭", "en": "close-up shot, sharp focus"},
                    "2": {"ch": "完美商務中景鏡頭", "en": "medium shot, professional corporate framing"},
                    "3": {"ch": "大器環境廣角鏡頭", "en": "wide-angle shot showing majestic environment"},
                    "4": {"ch": "85mm 大光圈人像鏡", "en": "shot on 85mm lens, f/1.4, shallow depth of field, creamy blurred background"},
                    "5": {"ch": "35mm 人文寫實紀錄鏡", "en": "35mm lens documentary style, authentic storytelling"},
                    "6": {"ch": "細節聚焦微距鏡頭", "en": "macro detail shot, crisp textures"},
                    "7": {"ch": "低角度英雄氣勢仰拍", "en": "low-angle heroic shot, powerful perspective"},
                    "8": {"ch": "平視真實比例鏡頭", "en": "eye-level realistic perspective shot"},
                    "9": {"ch": "高角度大師級俯拍", "en": "high-angle dramatic cinematic placement"},
                    "10": {"ch": "長焦空間壓縮鏡頭", "en": "telephoto lens compression effect"},
                    "11": {"ch": "2.35:1 電影變形寬螢幕", "en": "anamorphic widescreen aspect ratio shot"},
                    "12": {"ch": "航拍鳥瞰宏偉全景", "en": "drone aerial masterpiece view"},
                    "13": {"ch": "魚眼創意獨特視角", "en": "creative fisheye lens distortion"},
                    "14": {"ch": "黃金比例構圖", "en": "perfect golden ratio composition"},
                    "15": {"ch": "動態瞬間高速快門捕捉", "en": "high-speed shutter, capturing dynamic motion freeze"}
                }
            }
        }

    def run_engine(self):
        print("\n" + "★"*31)
        print("★  日月鑫 15×8 智能繪圖提示詞生成矩陣  ★")
        print("★"*31)
        
        selections = {}
        order = ["Who", "Look", "Wear", "Action", "Where", "Light", "Style", "Camera"]
        
        for step, category in enumerate(order, 1):
            self.display_category(category)
            print("-" * 65)
            
            while True:
                user_input = input(f"【步驟 {step}/8】請選擇編號 (1-15)，或直接按 Enter 由系統智能配置: ").strip()
                if user_input == "":
                    user_input = str(random.randint(1, 15))
                    print(f" -> [系統推薦] 自動選擇: {user_input}")
                    break
                elif user_input.isdigit() and 1 <= int(user_input) <= 15:
                    break
                else:
                    print("[提示] 輸入無效，請輸入 1 至 15 之間的數字。")
            
            selections[category] = self.matrix[category]["options"][str(int(user_input))]
        
        self.output_final_prompt(selections)

    def display_category(self, category_key):
        data = self.matrix[category_key]
        print(f"\n==================== 【 {data['name']} 】 15大核心元素矩陣 ====================")
        items = list(data["options"].items())
        for i in range(0, len(items), 2):
            opt_id1, opt_data1 = items[i]
            str1 = f"[{opt_id1.zfill(2)}] {opt_data1['ch']}"
            if i + 1 < len(items):
                opt_id2, opt_data2 = items[i+1]
                str2 = f"[{opt_id2.zfill(2)}] {opt_data2['ch']}"
                print(f"{str1:<35}{str2}")
            else:
                print(str1)

    def output_final_prompt(self, selections):
        ch_formula = (
            f"一個{selections['Look']['ch']}的{selections['Who']['ch']}，"
            f"身穿{selections['Wear']['ch']}，"
            f"正在{selections['Action']['ch']}，"
            f"背景在{selections['Where']['ch']}。"
            f"畫面充滿{selections['Light']['ch']}，"
            f"呈現出{selections['Style']['ch']}，"
            f"並以{selections['Camera']['ch']}完成創作。"
        )
        en_prompt = (
            f"{selections['Who']['en']}, {selections['Look']['en']}, "
            f"{selections['Wear']['en']}, {selections['Action']['en']}, "
            f"{selections['Where']['en']}, {selections['Light']['en']}, "
            f"{selections['Style']['en']}, {selections['Camera']['en']}, "
            f"photorealistic, ultra-detailed, 8k resolution --ar 16:9 --v 6.0"
        )
        print("\n" + "■"*40)
        print("【系統生成報告：架構完美生成成功】")
        print("■"*40)
        print("\n● 中文語意精準對齊：")
        print(ch_formula)
        print("\n● 國際 AI 繪圖專用鏈結：")
        print(en_prompt)
        print("\n" + "■"*40)

if __name__ == "__main__":
    engine = ElitePromptEngine()
    while True:
        engine.run_engine()
        print("\n[1] 繼續生成下一張創意圖")
        print("[2] 關閉系統")
        choice = input("請選擇下一步運作模式: ").strip()
        if choice != "1":
            print("\n系統正常登出。祝您的創意項目取得圓滿成功，卓越非凡！")
            sys.exit()

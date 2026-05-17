import streamlit as st
import random

# 1. 網頁頂層旗艦商務配置
st.set_page_config(
    page_title="日月鑫管顧 | 商業視覺資產工廠 4.0",
    page_icon="🏭",
    layout="wide"
)

# 企業品牌大器標題
st.title("🏭 日月鑫商務視覺資產工廠 4.0")
st.subheader("打破「人本限制」：全面導入《數位時代》5大商業維度 × 100億級無死角矩陣")
st.markdown("本系統已將原始公式升級為：`[商業維度] + [風格] + [人種/本質] + [核心主體] + [外觀材質] + [包裝/點綴] + [動態/應用] + [背景] + [光線] + [格式]`，完美相容人物與非人物（如菜單、Icon、圖表、包裝）的全面生成。")
st.markdown("---")

# 2. 升級版 10×10 跨界商業資產大數據矩陣
matrix = {
    "Dimension": {
        "name": "01. 商業維度/場景類型 (Dimension) *新增",
        "options": {
            "1": {"ch": "品牌社群 | 形象廣告與商品照", "en": "Brand commercial advertising and product shot"},
            "2": {"ch": "品牌社群 | 輪播圖與資訊圖卡", "en": "Social media carousel and info-card layout"},
            "3": {"ch": "工作應用 | 商業簡報與提案封面", "en": "Professional corporate presentation and proposal cover design"},
            "4": {"ch": "工作應用 | 數據圖表與 Checklist 清單", "en": "Structured data visualization and checklist infographic"},
            "5": {"ch": "工作應用 | App Icon 與 UI 元素設計", "en": "Digital App Icon and user interface asset design"},
            "6": {"ch": "生活實用 | 商業菜單與設計文宣", "en": "Commercial menu design and creative flyer layout"},
            "7": {"ch": "生活實用 | 季節月曆與行程規劃表", "en": "Seasonal calendar and travel itinerary template layout"},
            "8": {"ch": "靈感點子 | LINE 貼圖與角色表情包", "en": "LINE sticker sheet collection, multiple character emoji expressions"},
            "9": {"ch": "靈感點子 | 四格漫畫與黑膠唱片封面", "en": "4-panel comic strip art and vinyl record album cover design"},
            "10": {"ch": "風格轉換 | 3D 黏土Q版與 Y2K 藝術特效", "en": "3D claymation pop-art and Y2K aesthetic retro transformation"}
        }
    },
    "Style": {
        "name": "02. 風格大類 (Style)",
        "options": {
            "1": {"ch": "極致寫實攝影", "en": "Hyper-realistic commercial photography, award-winning cinematography"},
            "2": {"ch": "富比士商務雜誌封面風", "en": "Modern Forbes business magazine cover style"},
            "3": {"ch": "吉卜力經典手繪動畫風", "en": "Classic Studio Ghibli anime hand-drawn illustration style"},
            "4": {"ch": "Y2K復古四格大頭貼風", "en": "Y2k retro nostalgic 4-panel photobooth sticker style"},
            "5": {"ch": "極簡幾何線條設計藝術", "en": "Minimalist clean line-art graphic design style"},
            "6": {"ch": "3D Octane 頂級渲染藝術", "en": "8k resolution, ultra-detailed 3D octane render art"},
            "7": {"ch": "迪士尼皮克斯 3D 動畫風", "en": "Whimsical Disney Pixar 3D animation style"},
            "8": {"ch": "經典復古膠卷底片風", "en": "Warm retro vintage film photography style"},
            "9": {"ch": "現代高端平面向量插畫", "en": "Modern clean vector flat illustration"},
            "10": {"ch": "新東方美學現代融合風", "en": "Modern oriental fusion aesthetic style"}
        }
    },
    "Race": {
        "name": "03. 人種/風格根源 (Race/Origin)",
        "options": {
            "1": {"ch": "東亞/亞洲（人物精準防呆）", "en": "East Asian"},
            "2": {"ch": "當代歐美人種風格", "en": "Western Caucasian"},
            "3": {"ch": "北歐簡約風底蘊", "en": "Scandinavian"},
            "4": {"ch": "日系文青簡約感", "en": "Japanese minimalist lifestyle"},
            "5": {"ch": "法式高奢時尚美學", "en": "French luxury fashion aesthetic"},
            "6": {"ch": "未來感科幻/半機械風", "en": "Futuristic cybernetic style"},
            "7": {"ch": "美式現代流行文化風", "en": "American pop culture style"},
            "8": {"ch": "義大利古典藝術工藝風", "en": "Italian classic artisan style"},
            "9": {"ch": "跨文化融合架構", "en": "Cross-cultural fusion"},
            "10": {"ch": "中性/通用物件（無人種限制）", "en": ""}
        }
    },
    "Who": {
        "name": "04. 核心主體 (Who/Subject) *通用化",
        "options": {
            "1": {"ch": "高階商務菁英人士", "en": "An elite corporate executive"},
            "2": {"ch": "創新創業領袖群", "en": "A visionary business leader"},
            "3": {"ch": "品牌吉祥物 IP 角色", "en": "A charismatic brand mascot character"},
            "4": {"ch": "實體商品/奢華包裝物件", "en": "A premium product with luxury packaging asset"},
            "5": {"ch": "數位 UI 介面/Icon/徽章", "en": "A clean digital interface element, icon asset"},
            "6": {"ch": "Q版 3D 立體公仔角色", "en": "A cute 3D chibi character asset"},
            "7": {"ch": "向量流程圖表/箭頭/框架", "en": "An organized vector flowchart diagram layout with clear arrows"},
            "8": {"ch": "擬人化可愛動物角色", "en": "An anthropomorphic adorable animal character"},
            "9": {"ch": "建築外觀/室內空間主體", "en": "A majestic architectural exterior and luxury interior workspace"},
            "10": {"ch": "時尚潮流頂級模特兒", "en": "A high-fashion stylized runway model"}
        }
    },
    "Look": {
        "name": "05. 外觀特徵/材質細節 (Look)",
        "options": {
            "1": {"ch": "優雅高貴/質感非凡", "en": "with an elegant and sophisticated premium texture"},
            "2": {"ch": "精明幹練/俐落線條", "en": "with sharp, professional and clean minimalist lines"},
            "3": {"ch": "輕鬆從容/自信自信", "en": "with a relaxed, confident and approachable vibe"},
            "4": {"ch": "睿智深思/富有內涵", "en": "with a wise, thoughtful and deep meaningful aesthetic"},
            "5": {"ch": "溫暖黏土手作立體質感", "en": "crafted in charming hand-made claymation matte texture"},
            "6": {"ch": "微縮樂高積木拼裝質感", "en": "designed in creative miniature Lego brick textures"},
            "7": {"ch": "高科技拉絲金屬與玻璃", "en": "made of brushed luxury metal and reflective transparent glass"},
            "8": {"ch": "復古斑駁/帶有歷史故事感", "en": "with a beautiful weathered retro vintage texture"},
            "9": {"ch": "空靈夢幻/超現實漸層色", "en": "with an ethereal dreamlike holographic gradient color palette"},
            "10": {"ch": "大膽鮮豔/對比強烈飽和色", "en": "with bold pop art high-contrast vivid color themes"}
        }
    },
    "Wear": {
        "name": "06. 服飾/外殼/包裝點綴 (Wear) *通用化",
        "options": {
            "1": {"ch": "高奢高級禮服/精緻外觀", "en": "adorned with magnificent luxury couture dress features"},
            "2": {"ch": "量身正裝西服/俐落外包裝", "en": "enclosed in a perfectly tailored luxury corporate suit outline"},
            "3": {"ch": "極簡質感運動風/俐落封邊", "en": "finished with premium minimalist sportswear details"},
            "4": {"ch": "Y2K復古街頭服飾/潮流裝飾", "en": "embellished with Y2K retro high-street fashion elements"},
            "5": {"ch": "未來機能感線條/幾何邊框", "en": "framed with futuristic tactical tech-wear lines and geometric cutouts"},
            "6": {"ch": "精緻編織毛線/針織布料質感", "en": "textured with cozy realistic knitted yarn and woven fabrics"},
            "7": {"ch": "英倫經典風衣/雙排扣點綴", "en": "styled with a timeless classic double-breasted trench coat frame"},
            "8": {"ch": "清爽亞麻襯衫/極簡標籤設計", "en": "complemented by a crisp premium minimalist textile tag"},
            "9": {"ch": "現代改良東方傳統刺繡工藝", "en": "detailed with elegant modern oriental fusion embroidered patterns"},
            "10": {"ch": "高檔柔軟羊絨/溫潤倒角保護殼", "en": "wrapped in an upscale soft cashmere premium finish"}
        }
    },
    "Action": {
        "name": "07. 核心動態/功能功能 (Action)",
        "options": {
            "1": {"ch": "品嚐咖啡/靜態展示", "en": "thoughtfully showcased in a static elegant pose"},
            "2": {"ch": "發表簡報/傳遞核心資訊", "en": "structured to effectively communicate key corporate messages"},
            "3": {"ch": "展示多種表情符號與動作包", "en": "displaying a balanced grid sheet of various expressions and poses"},
            "4": {"ch": "衝破手機螢幕的裸眼 3D 特效", "en": "bursting out of a smartphone screen with a 3D pop-out effect"},
            "5": {"ch": "自信前行/大器排版對齊", "en": "moving forward with a powerful stride aligned with graphic grids"},
            "6": {"ch": "分析多螢幕數據/清單打勾分類", "en": "analyzing complex data with clean checked checklist points"},
            "7": {"ch": "繪製未來藍圖/清晰流程引導", "en": "sketching a visionary corporate blueprint with clear visual guidance"},
            "8": {"ch": "舉杯慶祝/烘托成功高光時刻", "en": "toasting to celebrate triumph and business milestones"},
            "9": {"ch": "虛實整合/動態穿透分層", "en": "intertwining physical assets with digital holographic layers"},
            "10": {"ch": "極簡靜置/留白供文字排版", "en": "perfectly static with empty negative space for professional typography"}
        }
    },
    "Where": {
        "name": "08. 哪裡/背景環境 (Where)",
        "options": {
            "1": {"ch": "現代高階商務辦公室", "en": "inside a high-end modern corporate headquarters office"},
            "2": {"ch": "純色乾淨去背工作室背景", "en": "against a clean solid white studio background, isolated, die-cut"},
            "3": {"ch": "頂樓景觀奢華咖啡廳", "en": "at a luxury rooftop cafe overlooking the city skyline"},
            "4": {"ch": "向量資訊圖表簡潔排版空間", "en": "within a minimalist clean vector infographic layout, template style"},
            "5": {"ch": "未來賽博朋克霓虹街頭", "en": "on a futuristic cyberpunk neon-lit street"},
            "6": {"ch": "奢華五星級酒店大堂", "en": "inside the grand majestic lobby of a 5-star luxury hotel"},
            "7": {"ch": "大器高雅的私人圖書書房", "en": "in a prestigious private library with floor-to-ceiling books"},
            "8": {"ch": "海景第一排無邊際露台", "en": "on a breathtaking oceanfront terrace next to an infinity pool"},
            "9": {"ch": "工業風挑高頂級藝術工作室", "en": "in a spacious upscale industrial loft art studio"},
            "10": {"ch": "文青風手繪溫暖奶油色留白背景", "en": "against a cozy warm cream-colored hand-drawn blank canvas"}
        }
    },
    "Light": {
        "name": "09. 光線氛圍 (Light)",
        "options": {
            "1": {"ch": "高級自然側光", "en": "refined natural side lighting"},
            "2": {"ch": "溫慢黃金黃昏逆光", "en": "golden hour warm backlighting with soft sun flares"},
            "3": {"ch": "強烈對比醒目縮圖光", "en": "high-contrast vibrant dynamic lighting for mobile readability"},
            "4": {"ch": "柔和商務棚拍高級光", "en": "soft commercial studio portrait lighting"},
            "5": {"ch": "雙重曝光藝術光影 layout", "en": "creative double exposure artistic lighting layout"},
            "6": {"ch": "賽博朋克藍紫全息光", "en": "cyberpunk holographic glow with blue and purple tones"},
            "7": {"ch": "戲劇化明暗對比光影", "en": "dramatic chiaroscuro lighting for deep artistic contrast"},
            "8": {"ch": "夢幻電影耀光強光", "en": "dramatic lens flare with anamorphic streaks"},
            "9": {"ch": "神聖壯麗的耶穌光", "en": "volumetric god rays breaking through the background"},
            "10": {"ch": "乾淨透明無陰影高調光", "en": "clean, bright high-key lighting without harsh shadows"}
        }
    },
    "Format": {
        "name": "10. 輸出格式與後綴參數 (Format)",
        "options": {
            "1": {"ch": "LINE 貼圖專用格式 (1:1 白底去背貼紙包)", "en": "LINE sticker sheet design, emoji collection, isolated white background, die-cut outline --ar 1:1"},
            "2": {"ch": "Instagram 社群正方形貼文 (1:1 最佳留白)", "en": "Square post layout with negative space for social media marketing --ar 1:1"},
            "3": {"ch": "YouTube 醒目高點閱縮圖 (16:9 高明度)", "en": "YouTube thumbnail composition style, optimized for mobile readability --ar 16:9"},
            "4": {"ch": "商業簡報 PPT/Keynote 封面 (16:9 大器)", "en": "Corporate presentation master slide cover layout --ar 16:9"},
            "5": {"ch": "富比士風格直式雜誌封面 (2:3 黃金比例)", "en": "Vertical premium magazine cover orientation --ar 2:3"},
            "6": {"ch": "好萊塢電影寬螢幕巨幕 (21:9 震撼視角)", "en": "Cinematic ultra-widescreen majestic framing --ar 21:9"},
            "7": {"ch": "數位看板/電子屏幕橫式廣告 (16:10 標準)", "en": "Digital signage display banner format --ar 16:10"},
            "8": {"ch": "手機壁紙/直式限時動態 (9:16 全螢幕)", "en": "Mobile wallpaper orientation, Instagram Stories layout --ar 9:16"},
            "9": {"ch": "標準海報印刷大尺寸比例 (3:4 卓越構圖)", "en": "Standard print poster asset aspect ratio --ar 3:4"},
            "10": {"ch": "4K/8K 國際高畫質標準規格 (16:9 通用)", "en": "Universal ultra-high-definition television standard format --ar 16:9"}
        }
    }
}

# 3. 戰略矩陣交互介面排版 (2列×5欄)
st.write("### ⚙️ 數位資產維度配置面版")
order = ["Dimension", "Style", "Race", "Who", "Look", "Wear", "Action", "Where", "Light", "Format"]
selections = {}

col_group1 = st.columns(5)
col_group2 = st.columns(5)
all_cols = col_group1 + col_group2

for idx, category in enumerate(order):
    data = matrix[category]
    display_options = [f"[{k.zfill(2)}] {v['ch']}" for k, v in data["options"].items()]
    
    with all_cols[idx]:
        user_choice = st.selectbox(
            label=data["name"],
            options=display_options,
            index=0
        )
        selected_key = str(int(user_choice.split("]")[0].replace("[", "")))
        selections[category] = data["options"][selected_key]

st.markdown("---")

if st.button("🎲 啟動百億級別全領域交叉創新配置"):
    for category in order:
        random_key = random.choice(list(matrix[category]["options"].keys()))
        selections[category] = matrix[category]["options"][random_key]
    st.toast("已完成跨維度（人物/資產/圖表）隨機配置！", icon="🏭")

# 4. 線性鏈結與指令報告輸出
st.write("### 🚀 旗艦級商業視覺指令產出報告")

race_en = f"{selections['Race']['en']} " if selections['Race']['en'] else ""
en_prompt = (
    f"{selections['Dimension']['en']}, {selections['Style']['en']}, {race_en}{selections['Who']['en']}, "
    f"{selections['Look']['en']}, {selections['Wear']['en']}, {selections['Action']['en']}, "
    f"{selections['Where']['en']}, {selections['Light']['en']}, {selections['Format']['en']}, "
    f"photorealistic, ultra-detailed, 8k resolution"
).replace(", ,", ",").strip()

st.success("🎨 **國際 AI 繪圖專用鏈結（全場景通用版，請直接複製使用）**")
st.code(en_prompt, language="text")

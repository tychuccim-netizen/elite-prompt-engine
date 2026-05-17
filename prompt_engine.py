import streamlit as st
import random

# 1. 網頁頂層旗艦商務配置
st.set_page_config(
    page_title="日月鑫管顧 | 商業視覺資產工廠 5.0",
    page_icon="🏭",
    layout="wide"
)

# 企業品牌大器標題
st.title("🏭 日月鑫商務視覺資產工廠 5.0")
st.subheader("解構《數位時代》5大商業維度 × 中英雙語 AI 專用結構化標籤鏈結系統")
st.markdown("本系統已全面打通「中文繪圖引擎」與「國際英文引擎」的底層權限，支援一鍵生成雙語標籤，確保品牌在智能化營運中保持絕對領先。")
st.markdown("---")

# 2. 10×10 跨界商業資產大數據矩陣數據庫
matrix = {
    "Dimension": {
        "name": "01. 商業維度/場景類型 (Dimension)",
        "options": {
            "1": {"ch": "品牌社群、形象廣告、商品照", "en": "Brand commercial advertising and product shot"},
            "2": {"ch": "品牌社群、輪播圖、資訊圖卡 layout", "en": "Social media carousel and info-card layout"},
            "3": {"ch": "工作應用、商業簡報、提案封面設計", "en": "Professional corporate presentation and proposal cover design"},
            "4": {"ch": "工作應用、數據圖表、Checklist 清單資訊圖", "en": "Structured data visualization and checklist infographic"},
            "5": {"ch": "工作應用、App Icon、UI 元素設計", "en": "Digital App Icon and user interface asset design"},
            "6": {"ch": "生活實用、商業菜單、設計文宣", "en": "Commercial menu design and creative flyer layout"},
            "7": {"ch": "生活實用、季節月曆、行程規劃表", "en": "Seasonal calendar and travel itinerary template layout"},
            "8": {"ch": "靈感點子、LINE 貼圖、角色表情包", "en": "LINE sticker sheet collection, multiple character emoji expressions"},
            "9": {"ch": "靈感點子、四格漫畫、黑膠唱片封面", "en": "4-panel comic strip art and vinyl record album cover design"},
            "10": {"ch": "風格轉換、3D 黏土Q版、Y2K 藝術特效", "en": "3D claymation pop-art and Y2K aesthetic retro transformation"}
        }
    },
    "Style": {
        "name": "02. 風格大類 (Style)",
        "options": {
            "1": {"ch": "極致寫實攝影、得獎電影級採光", "en": "Hyper-realistic commercial photography, award-winning cinematography"},
            "2": {"ch": "富比士商務雜誌封面風格", "en": "Modern Forbes business magazine cover style"},
            "3": {"ch": "吉卜力經典手繪動畫風格", "en": "Classic Studio Ghibli anime hand-drawn illustration style"},
            "4": {"ch": "Y2K復古四格大頭貼風格", "en": "Y2k retro nostalgic 4-panel photobooth sticker style"},
            "5": {"ch": "極簡幾何線條設計藝術", "en": "Minimalist clean line-art graphic design style"},
            "6": {"ch": "3D Octane 頂級渲染藝術", "en": "8k resolution, ultra-detailed 3D octane render art"},
            "7": {"ch": "迪士尼皮克斯 3D 動畫風格", "en": "Whimsical Disney Pixar 3D animation style"},
            "8": {"ch": "經典復古膠卷底片風格", "en": "Warm retro vintage film photography style"},
            "9": {"ch": "現代高端平面向量插畫", "en": "Modern clean vector flat illustration"},
            "10": {"ch": "新東方美學現代融合風", "en": "Modern oriental fusion aesthetic style"}
        }
    },
    "Race": {
        "name": "03. 人種/風格根源 (Race/Origin)",
        "options": {
            "1": {"ch": "東亞人、亞洲面孔（精準防呆）", "en": "East Asian"},
            "2": {"ch": "當代歐美人種風格", "en": "Western Caucasian"},
            "3": {"ch": "北歐簡約風底蘊", "en": "Scandinavian"},
            "4": {"ch": "日系文青簡約感", "en": "Japanese minimalist lifestyle"},
            "5": {"ch": "法式高奢時尚美學", "en": "French luxury fashion aesthetic"},
            "6": {"ch": "未來感科幻半機械風", "en": "Futuristic cybernetic style"},
            "7": {"ch": "美式現代流行文化風", "en": "American pop culture style"},
            "8": {"ch": "義大利古典藝術工藝風", "en": "Italian classic artisan style"},
            "9": {"ch": "跨文化融合架構", "en": "Cross-cultural fusion"},
            "10": {"ch": "中性/通用物件（無人種限制）", "en": ""}
        }
    },
    "Who": {
        "name": "04. 核心主體 (Who/Subject)",
        "options": {
            "1": {"ch": "高階商務菁英女士", "en": "An elite businesswoman"},
            "2": {"ch": "高階商務菁英男士", "en": "An elite businessman"},
            "3": {"ch": "創新創業領袖群", "en": "A visionary business leader"},
            "4": {"ch": "品牌吉祥物 IP 角色", "en": "A charismatic brand mascot character"},
            "5": {"ch": "實體商品、奢華包裝物件", "en": "A premium product with luxury packaging asset"},
            "6": {"ch": "數位 UI 介面、Icon、徽章", "en": "A clean digital interface element, icon asset"},
            "7": {"ch": "Q版 3D 立體公仔角色", "en": "A cute 3D chibi character asset"},
            "8": {"ch": "向量流程圖表、箭頭引導、框架", "en": "An organized vector flowchart diagram layout with clear arrows"},
            "9": {"ch": "擬人化可愛動物角色", "en": "An anthropomorphic adorable animal character"},
            "10": {"ch": "時尚潮流頂級模特兒", "en": "A high-fashion stylized runway model"}
        }
    },
    "Look": {
        "name": "05. 外觀特徵/材質細節 (Look)",
        "options": {
            "1": {"ch": "優雅高貴、質感非凡", "en": "with an elegant and sophisticated premium texture"},
            "2": {"ch": "精明幹練、俐落線條", "en": "with sharp, professional and clean minimalist lines"},
            "3": {"ch": "輕鬆從容、自信微笑", "en": "with a relaxed, confident and approachable vibe"},
            "4": {"ch": "睿智深思、富有內涵美學", "en": "with a wise, thoughtful and deep meaningful aesthetic"},
            "5": {"ch": "溫暖黏土手作立體質感", "en": "crafted in charming hand-made claymation matte texture"},
            "6": {"ch": "微縮樂高積木拼裝質感", "en": "designed in creative miniature Lego brick textures"},
            "7": {"ch": "高科技拉絲金屬、反射鋼化玻璃", "en": "made of brushed luxury metal and reflective transparent glass"},
            "8": {"ch": "復古斑駁、帶有歷史故事感", "en": "with a beautiful weathered retro vintage texture"},
            "9": {"ch": "空靈夢幻、超現實漸層色彩", "en": "with an ethereal dreamlike holographic gradient color palette"},
            "10": {"ch": "大膽鮮豔、對比強烈高飽和度色調", "en": "with bold pop art high-contrast vivid color themes"}
        }
    },
    "Wear": {
        "name": "06. 服飾/外殼/包裝點綴 (Wear)",
        "options": {
            "1": {"ch": "身穿高級奢華禮服", "en": "adorned with magnificent luxury couture dress features"},
            "2": {"ch": "身穿量身定制正裝西服", "en": "enclosed in a perfectly tailored luxury corporate suit outline"},
            "3": {"ch": "俐落商務西裝套裝", "en": "wearing a sleek corporate blazer"},
            "4": {"ch": "Y2K復古高街潮流服飾裝飾", "en": "embellished with Y2K retro high-street fashion elements"},
            "5": {"ch": "未來機能感線條、幾何邊框裝框", "en": "framed with futuristic tactical tech-wear lines and geometric cutouts"},
            "6": {"ch": "精緻編織毛線、針織布料質感包覆", "en": "textured with cozy realistic knitted yarn and woven fabrics"},
            "7": {"ch": "英倫經典風衣外殼", "en": "styled with a timeless classic double-breasted trench coat frame"},
            "8": {"ch": "清爽亞麻襯衫、極簡標籤設計", "en": "complemented by a crisp premium minimalist textile tag"},
            "9": {"ch": "現代改良東方傳統刺繡工藝圖騰", "en": "detailed with elegant modern oriental fusion embroidered patterns"},
            "10": {"ch": "高檔柔軟羊絨質感護殼", "en": "wrapped in an upscale soft cashmere premium finish"}
        }
    },
    "Action": {
        "name": "07. 核心動態/功能動態 (Action)",
        "options": {
            "1": {"ch": "輕鬆品嚐頂級咖啡", "en": "thoughtfully showcased in a static elegant pose"},
            "2": {"ch": "發表簡報、精準傳遞核心資訊", "en": "structured to effectively communicate key corporate messages"},
            "3": {"ch": "展示多種表情符號與動作貼圖組合", "en": "displaying a balanced grid sheet of various expressions and poses"},
            "4": {"ch": "衝破手機螢幕的裸眼 3D 特效動態", "en": "bursting out of a smartphone screen with a 3D pop-out effect"},
            "5": {"ch": "自信前行、大器網格排版對齊", "en": "moving forward with a powerful stride aligned with graphic grids"},
            "6": {"ch": "分析多螢幕數據、清單打勾分類引導", "en": "analyzing complex data with clean checked checklist points"},
            "7": {"ch": "繪製未來藍圖、清晰流程視覺引導", "en": "sketching a visionary corporate blueprint with clear visual guidance"},
            "8": {"ch": "舉杯慶祝、烘托成功高光時刻", "en": "toasting to celebrate triumph and business milestones"},
            "9": {"ch": "虛實整合、動態穿透分層視覺", "en": "intertwining physical assets with digital holographic layers"},
            "10": {"ch": "極簡靜置、保留大量空白供文字排版", "en": "perfectly static with empty negative space for professional typography"}
        }
    },
    "Where": {
        "name": "08. 哪裡/背景環境 (Where)",
        "options": {
            "1": {"ch": "背景在現代高階商務辦公室內部", "en": "inside a high-end modern corporate headquarters office"},
            "2": {"ch": "純色乾淨去背工作室背景、獨立物件", "en": "against a clean solid white studio background, isolated, die-cut"},
            "3": {"ch": "頂樓景觀奢華咖啡廳、俯瞰城市天際線", "en": "at a luxury rooftop cafe overlooking the city skyline"},
            "4": {"ch": "向量資訊圖表簡潔排版空間背景", "en": "within a minimalist clean vector infographic layout, template style"},
            "5": {"ch": "未來賽博朋克霓虹燈光街頭背景", "en": "on a futuristic cyberpunk neon-lit street"},
            "6": {"ch": "奢華五星級酒店大堂中央", "en": "inside the grand majestic lobby of a 5-star luxury hotel"},
            "7": {"ch": "大器高雅的私人圖書室、通頂書牆背景", "en": "in a prestigious private library with floor-to-ceiling books"},
            "8": {"ch": "海景第一排無邊際露台、臨近無邊際泳池", "en": "on a breathtaking oceanfront terrace next to an infinity pool"},
            "9": {"ch": "工業風挑高頂級藝術工作室空間", "en": "in a spacious upscale industrial loft art studio"},
            "10": {"ch": "文青風手繪溫暖奶油色留白背景底層", "en": "against a cozy warm cream-colored hand-drawn blank canvas"}
        }
    },
    "Light": {
        "name": "09. 光線氛圍 (Light)",
        "options": {
            "1": {"ch": "高級自然側光、細膩陰影", "en": "refined natural side lighting"},
            "2": {"ch": "溫暖黃金黃昏逆光、柔和耀光", "en": "golden hour warm backlighting with soft sun flares"},
            "3": {"ch": "強烈對比醒目縮圖光、高辨識度高明度", "en": "high-contrast vibrant dynamic lighting for mobile readability"},
            "4": {"ch": "柔和商務棚拍高級商用光影", "en": "soft commercial studio portrait lighting"},
            "5": {"ch": "雙重曝光藝術光影版面", "en": "creative double exposure artistic lighting layout"},
            "6": {"ch": "賽博朋克藍紫雙色全息光芒", "en": "cyberpunk holographic glow with blue and purple tones"},
            "7": {"ch": "戲劇化明暗對比光影、深邃藝術感", "en": "dramatic chiaroscuro lighting for deep artistic contrast"},
            "8": {"ch": "夢幻電影耀光、變形寬銀幕光斑", "en": "dramatic lens flare with anamorphic streaks"},
            "9": {"ch": "神聖壯麗的耶穌光、丁達爾效應光束", "en": "volumetric god rays breaking through the background"},
            "10": {"ch": "乾淨透明無陰影高調光、透亮感", "en": "clean, bright high-key lighting without harsh shadows"}
        }
    },
    "Format": {
        "name": "10. 輸出格式與後綴參數 (Format)",
        "options": {
            "1": {"ch": "LINE貼圖格式、1:1比例、白邊去背貼紙包貼紙", "en": "LINE sticker sheet design, emoji collection, isolated white background, die-cut outline --ar 1:1"},
            "2": {"ch": "Instagram社群正方形貼文排版、1:1比例最佳留白", "en": "Square post layout with negative space for social media marketing --ar 1:1"},
            "3": {"ch": "YouTube醒目高點閱縮圖視覺、16:9比例高明度", "en": "YouTube thumbnail composition style, optimized for mobile readability --ar 16:9"},
            "4": {"ch": "商業簡報 PPT/Keynote 封面視覺、16:9寬螢幕大器構圖", "en": "Corporate presentation master slide cover layout --ar 16:9"},
            "5": {"ch": "富比士風格直式雜誌封面、2:3黃金比例排版", "en": "Vertical premium magazine cover orientation --ar 2:3"},
            "6": {"ch": "好萊塢電影寬螢幕巨幕、21:9震撼電影視角", "en": "Cinematic ultra-widescreen majestic framing --ar 21:9"},
            "7": {"ch": "數位看板/電子屏幕橫式廣告 banner、16:10標準規格", "en": "Digital signage display banner format --ar 16:10"},
            "8": {"ch": "手機壁紙/直式限時動態海報、9:16全螢幕視覺", "en": "Mobile wallpaper orientation, Instagram Stories layout --ar 9:16"},
            "9": {"ch": "標準海報印刷大尺寸比例、3:4卓越非凡構圖", "en": "Standard print poster asset aspect ratio --ar 3:4"},
            "10": {"ch": "4K/8K國際高畫質標準規格、16:9通用大氣視角", "en": "Universal ultra-high-definition television standard format --ar 16:9"}
        }
    }
}

# 3. 戰略矩陣交互介面排版 (2列×5欄)
st.write("### ⚙️ 全領域商務資產維度配置面版")
order = ["Dimension", "Style", "Race", "Who", "Look", "Wear", "Action", "Where", "Light", "Format"]
selections = {}

col_group1 = st.columns(5)
col_group2 = st.columns(5)
all_cols = col_group1 + col_group2

for idx, category in enumerate(order):
    data = matrix[category]
    display_options = [f"[{k.zfill(2)}] {v['ch']}" for k, v in data["options"].items()]
    
    with all_cols[idx]:
        user_choice = st.selectbox(label=data["name"], options=display_options, index=0)
        selected_key = str(int(user_choice.split("]")[0].replace("[", "")))
        selections[category] = data["options"][selected_key]

st.markdown("---")

if st.button("🎲 啟動 10×10 百億級別全領域跨界創新配置"):
    for category in order:
        random_key = random.choice(list(matrix[category]["options"].keys()))
        selections[category] = matrix[category]["options"][random_key]
    st.toast("已完成全維度標籤化交叉隨機配置！", icon="🏭")

# 4. 線性鏈結與指令報告輸出
st.write("### 🚀 旗艦級雙語商業視覺指令產出報告")

# 【人類語意檢視】
ch_formula = (
    f"【當前配置摘要】：這是一張針對【{selections['Dimension']['ch']}】所設計的視覺。風格鎖定【{selections['Style']['ch']}】。 "
    f"主體核心為【{selections['Race']['ch'] if selections['Race']['ch'] else '通用物件'}{selections['Who']['ch']}】，展現出【{selections['Look']['ch']}】並【{selections['Wear']['ch']}】。 "
    f"動態特徵為【{selections['Action']['ch']}】，環境設定在【{selections['Where']['ch']}】。畫面融入【{selections['Light']['ch']}】，並以【{selections['Format']['ch']}】高規格交付。"
)
st.info("💡 **中文語意架構流暢檢視（供人類團隊確認語意）**")
st.write(ch_formula)

st.markdown("---")

# 拆分兩欄：左側放中文引擎專用標籤鏈結，右側放國際英文引擎鏈結
col_output_ch, col_output_en = st.columns(2)

with col_output_ch:
    st.markdown("### 🇨🇳 中文 AI 繪圖專用鏈結 (Tag Chain)")
    race_ch_tag = f"{selections['Race']['ch']}, " if selections['Race']['ch'] else ""
    ch_prompt = (
        f"{selections['Dimension']['ch']}, {selections['Style']['ch']}, {race_ch_tag}{selections['Who']['ch']}, "
        f"{selections['Look']['ch']}, {selections['Wear']['ch']}, {selections['Action']['ch']}, "
        f"{selections['Where']['ch']}, {selections['Light']['ch']}, {selections['Format']['ch']}, "
        f"商業級質感, 寫實細節, 8K超高解析度"
    ).replace(", ,", ",").strip()
    st.code(ch_prompt, language="text")
    st.caption("※ 適合直接複製投入：文心一格、國內優化版 SD 繪圖大模型、或支援中文提示詞之繪圖引擎。")

with col_output_en:
    st.markdown("### 🇺🇸 國際 AI 繪圖專用鏈結 (English)")
    race_en_tag = f"{selections['Race']['en']} " if selections['Race']['en'] else ""
    en_prompt = (
        f"{selections['Style']['en']}, {selections['Camera']['en']}, {race_en_tag}{selections['Who']['en']}, "
        f"{selections['Look']['en']}, {selections['Wear']['en']}, {selections['Action']['en']}, "
        f"{selections['Where']['en']}, {selections['Light']['en']}, {selections['Format']['en']}, "
        f"photorealistic, ultra-detailed, 8k resolution"
    ).replace(", ,", ",").strip()
    st.code(en_prompt, language="text")
    st.caption("※ 適合直接複製投入：Midjourney、Stable Diffusion 原生大模型、DALL-E 3 等國際引擎。")

import streamlit as st
import random

# 1. 網頁頂層旗艦商務配置
st.set_page_config(
    page_title="日月鑫管顧 | 商業視覺資產工廠 5.1",
    page_icon="🏭",
    layout="wide"
)

# 企業品牌大器標題
st.title("🏭 日月鑫商務視覺資產工廠 5.1")
st.subheader("解構《數位時代》5大商業維度 × 中英雙語 AI 專用結構化標籤鏈結系統")
st.markdown("本系統已全面修復底層鏈結架構並移除國旗標識，完美支援「中文繪圖引擎」與「國際英文引擎」的雙語標籤產出。")
st.markdown("---")

# 2. 11×10 跨界商業資產大數據矩陣數據庫 (完整保留鏡頭與格式)
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
            "2": {"ch": "當代歐慢人種風格", "en": "Western Caucasian"},
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
            "5": {"ch": "溫慢黏土手作立體質感", "en": "crafted in charming hand-made claymation matte texture"},
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
            "2": {"ch": "發表簡報、精準傳遞核心

import os
import re

DOCS_DIR = os.path.abspath("docs")
ZH_DOCS_DIR = os.path.join(DOCS_DIR, "zh-CN")

SYNC_SCRIPT = """<script id="quarto-lang-switch-sync">
document.addEventListener('DOMContentLoaded', function() {
  var isZh = window.location.pathname.indexOf('/zh-CN/') !== -1;
  var path = window.location.pathname;
  var hash = window.location.hash || '';
  
  var links = document.querySelectorAll('a[aria-label="中文版"], a[aria-label="English"]');
  links.forEach(function(link) {
    var target = '';
    if (isZh) {
      target = path.replace('/zh-CN/', '/');
    } else {
      if (path.endsWith('/') || path.endsWith('/index.html')) {
        target = path.replace(/\\/index\\.html$/, '').replace(/\\/$/, '') + '/zh-CN/index.html';
      } else {
        target = path.replace('/Chapters/', '/zh-CN/Chapters/');
      }
    }
    if (target) {
      link.setAttribute('href', target + hash);
    }
  });
});
</script>
"""

def update_english_pages():
    index_path = os.path.join(DOCS_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        zh_btn = '<a href="./zh-CN/index.html" title="切换到中文版" class="quarto-navigation-tool px-1" aria-label="中文版"><i class="bi bi-globe"></i> <span style="font-size: 0.85rem; font-weight: 500;">中文</span></a>'
        if 'aria-label="中文版"' not in content:
            content = content.replace('<div class="sidebar-tools-main">\n  <a href="" class="quarto-color-scheme-toggle',
                                      f'<div class="sidebar-tools-main">\n  {zh_btn}\n  <a href="" class="quarto-color-scheme-toggle')
        
        if 'id="quarto-lang-switch-sync"' not in content:
            content = content.replace('</body>', f'{SYNC_SCRIPT}\n</body>')
            
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated docs/index.html")

    ch_dir = os.path.join(DOCS_DIR, "Chapters")
    if os.path.exists(ch_dir):
        for fname in os.listdir(ch_dir):
            if fname.endswith(".html"):
                fpath = os.path.join(ch_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                zh_btn = f'<a href="../zh-CN/Chapters/{fname}" title="切换到中文版" class="quarto-navigation-tool px-1" aria-label="中文版"><i class="bi bi-globe"></i> <span style="font-size: 0.85rem; font-weight: 500;">中文</span></a>'
                if 'aria-label="中文版"' not in content:
                    content = content.replace('<div class="sidebar-tools-main">\n  <a href="" class="quarto-color-scheme-toggle',
                                              f'<div class="sidebar-tools-main">\n  {zh_btn}\n  <a href="" class="quarto-color-scheme-toggle')
                
                if 'id="quarto-lang-switch-sync"' not in content:
                    content = content.replace('</body>', f'{SYNC_SCRIPT}\n</body>')
                    
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
        print(f"Updated all {len(os.listdir(ch_dir))} docs/Chapters/*.html")

def update_chinese_pages():
    index_path = os.path.join(ZH_DOCS_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        en_btn = '<a href="./../index.html" title="English" class="quarto-navigation-tool px-1" aria-label="English"><i class="bi bi-globe"></i> <span style="font-size: 0.85rem; font-weight: 500;">English</span></a>'
        content = re.sub(r'<a href="[^"]*" title="English" class="quarto-navigation-tool px-1" aria-label="English"><i class="bi bi-globe"></i>.*?</a>',
                         en_btn, content)
                         
        if 'id="quarto-lang-switch-sync"' not in content:
            content = content.replace('</body>', f'{SYNC_SCRIPT}\n</body>')
            
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated docs/zh-CN/index.html")

    ch_dir = os.path.join(ZH_DOCS_DIR, "Chapters")
    if os.path.exists(ch_dir):
        for fname in os.listdir(ch_dir):
            if fname.endswith(".html"):
                fpath = os.path.join(ch_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                en_btn = f'<a href="../../Chapters/{fname}" title="English" class="quarto-navigation-tool px-1" aria-label="English"><i class="bi bi-globe"></i> <span style="font-size: 0.85rem; font-weight: 500;">English</span></a>'
                content = re.sub(r'<a href="[^"]*" title="English" class="quarto-navigation-tool px-1" aria-label="English"><i class="bi bi-globe"></i>.*?</a>',
                                 en_btn, content)
                
                content = re.sub(r'(<a class="dropdown-item" href=")[^"]*(">\s*<span class="dropdown-text">English</span>)',
                                 rf'\1../../Chapters/{fname}\2', content)
                
                if 'id="quarto-lang-switch-sync"' not in content:
                    content = content.replace('</body>', f'{SYNC_SCRIPT}\n</body>')
                    
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
        print(f"Updated all {len(os.listdir(ch_dir))} docs/zh-CN/Chapters/*.html")

if __name__ == "__main__":
    update_english_pages()
    update_chinese_pages()

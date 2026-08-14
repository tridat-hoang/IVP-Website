import glob

files = glob.glob('c:/Users/Admin/Claude/Projects/IVP Website/*.html')
old_footer = '''  <p><a href="https://www.facebook.com/CaygiongIVP/">https://www.facebook.com/CaygiongIVP/</a></p>
  <p><a href="https://www.facebook.com/profile.php?id=61574868823364">FanPage https://www.facebook.com/profile.php?id=61574868823364</a></p>'''

new_footer = '''  <p><a href="https://www.facebook.com/share/18zuzNBw47/" target="_blank" rel="noopener">Cây Giống IVP</a></p>
  <p><a href="https://www.facebook.com/share/19Tj2G7ocB/" target="_blank" rel="noopener">Trung tâm Nuôi cấy mô IVP</a></p>
  <p><a href="https://www.facebook.com/share/1D17rWAX2a/" target="_blank" rel="noopener">IVP Plant</a></p>'''

old_contact = '<p><a href="https://www.facebook.com/CaygiongIVP/" target="_blank" rel="noopener">facebook.com/CaygiongIVP</a></p>'
new_contact = '''<p><a href="https://www.facebook.com/share/18zuzNBw47/" target="_blank" rel="noopener">Cây Giống IVP</a></p>
        <p><a href="https://www.facebook.com/share/19Tj2G7ocB/" target="_blank" rel="noopener">Trung tâm Nuôi cấy mô IVP</a></p>
        <p><a href="https://www.facebook.com/share/1D17rWAX2a/" target="_blank" rel="noopener">IVP Plant</a></p>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace(old_footer, new_footer)
    if 'contacts.html' in f:
        content = content.replace(old_contact, new_contact)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Updated all facebook links.')

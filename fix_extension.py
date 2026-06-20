content = open('extension.hbs').read()
content = content[:content.index('</body>')]
content += """  <script>
function copyText(btn, text) {
  if (!text || text.trim() === '' || text === 'undefined') {
    btn.textContent = 'Empty!';
    setTimeout(() => btn.textContent = 'Copy', 1500);
    return;
  }
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.focus();
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
  btn.textContent = 'Copied!';
  btn.classList.add('copied');
  setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1500);
}
  </script>
</body>
</html>"""
open('extension.hbs', 'w').write(content)
print('Done')

content = open('extension.hbs').read()

# Replace all onclick copyText patterns with data-attribute approach
import re
content = re.sub(
    r'<button class="copy-btn" onclick="copyText\(this, \'{{this\.(.*?)}}\'\)">Copy</button>',
    r'<button class="copy-btn" data-val="{{this.\1}}">Copy</button>',
    content
)

# Replace the script
old_script_start = content.index('<script>')
old_script_end = content.rindex('</script>') + len('</script>')
new_script = """<script>
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.copy-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var text = btn.getAttribute('data-val');
      if (!text || text.trim() === '') {
        btn.textContent = 'Empty!';
        setTimeout(function() { btn.textContent = 'Copy'; }, 1500);
        return;
      }
      var ta = document.createElement('textarea');
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
      setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1500);
    });
  });
});
</script>
</body>
</html>"""

content = content[:old_script_start] + new_script
open('extension.hbs', 'w').write(content)
print('Done')

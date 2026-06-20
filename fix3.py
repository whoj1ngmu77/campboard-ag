template = open('extension.hbs').read()

# Find where the info-card div starts and replace the whole template
new_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Info — CAMPUShelp</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { min-height: 100%; font-family: Inter, Arial, sans-serif; background: #080d13; color: #fff; }
    nav { display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; background: rgba(20,20,20,0.8); backdrop-filter: blur(8px); border-bottom: 1px solid rgba(0,255,252,0.15); position: sticky; top: 0; z-index: 10; }
    nav h1 { color: #00fffc; font-size: 1.2rem; }
    .btn { padding: 0.5rem 1.2rem; border-radius: 8px; font-size: 0.9rem; font-weight: 600; cursor: pointer; text-decoration: none; transition: all 0.2s; display: inline-block; }
    .btn-primary { background: linear-gradient(90deg, #00fffc, #26d0ce); color: #000; border: none; }
    .btn-danger { border: 1.5px solid #ff6b6b; color: #ff6b6b; background: transparent; }
    .btn-danger:hover { background: rgba(255,107,107,0.1); }
    .container { max-width: 900px; margin: 2.5rem auto; padding: 0 1.5rem; }
    .page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
    .page-header h2 { color: #00fffc; font-size: 1.4rem; }
    .info-card { background: rgba(20,20,20,0.75); border: 1.5px solid rgba(0,255,252,0.18); border-radius: 16px; padding: 2rem; box-shadow: 0 8px 32px rgba(0,255,252,0.08); margin-bottom: 1.5rem; }
    .section-title { color: #00fffc99; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid rgba(0,255,252,0.15); padding-bottom: 0.4rem; margin-bottom: 1rem; margin-top: 1.2rem; }
    .section-title:first-child { margin-top: 0; }
    .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; }
    .info-item { display: flex; flex-direction: column; gap: 0.3rem; }
    .info-label { font-size: 0.75rem; color: #666; text-transform: uppercase; letter-spacing: 0.5px; }
    .info-value-row { display: flex; align-items: center; gap: 0.5rem; }
    .info-value { color: #fff; font-size: 0.95rem; }
    .copy-btn { background: rgba(0,255,252,0.1); border: 1px solid rgba(0,255,252,0.3); color: #00fffc; padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.75rem; cursor: pointer; transition: all 0.2s; }
    .copy-btn:hover { background: rgba(0,255,252,0.2); }
    .copy-btn.copied { color: #26d0ce; border-color: #26d0ce; }
    .empty-state { text-align: center; padding: 4rem 2rem; background: rgba(20,20,20,0.75); border: 1.5px solid rgba(0,255,252,0.18); border-radius: 16px; }
    .empty-state p { color: #aaa; margin-bottom: 1rem; }
    table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
    th { background: rgba(0,255,252,0.1); color: #00fffc; padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid rgba(0,255,252,0.2); font-size: 0.8rem; text-transform: uppercase; }
    td { padding: 0.75rem 1rem; border-bottom: 1px solid rgba(255,255,255,0.05); color: #ccc; }
    td a { color: #00fffc; text-decoration: none; }
  </style>
</head>
<body>
  <nav>
    <h1>Welcome, {{user.name}}</h1>
    <a href="/logout" class="btn btn-danger">Logout</a>
  </nav>

  <div class="container">
    <div class="page-header">
      <h2>Your Stored Information</h2>
      <a href="/data" class="btn btn-primary">+ Add New Entry</a>
    </div>

    <div id="entries-container"></div>

    {{#unless dataEntries}}
    <div class="empty-state">
      <p>No information saved yet.</p>
      <a href="/data" class="btn btn-primary">Add Your First Entry</a>
    </div>
    {{/unless}}
  </div>

  <script>
    var entries = {{{json dataEntries}}};
    var container = document.getElementById('entries-container');

    function field(label, value) {
      return '<div class="info-item">' +
        '<span class="info-label">' + label + '</span>' +
        '<div class="info-value-row">' +
        '<span class="info-value">' + (value || '-') + '</span>' +
        '<button class="copy-btn" onclick="copyMe(this, \'' + (value || '') + '\')">Copy</button>' +
        '</div></div>';
    }

    function copyMe(btn, text) {
      if (!text || text.trim() === '') {
        btn.textContent = 'Empty!';
        setTimeout(function() { btn.textContent = 'Copy'; }, 1500);
        return;
      }
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.cssText = 'position:fixed;opacity:0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      btn.textContent = 'Copied!';
      btn.classList.add('copied');
      setTimeout(function() { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1500);
    }

    entries.forEach(function(e) {
      var html = '<div class="info-card">' +
        '<div class="section-title">Personal Details</div>' +
        '<div class="info-grid">' +
        field('Full Name', e.name) +
        field('Mobile', e.mobileNumber) +
        field('Email', e.emailId) +
        field('Aadhar Number', e.adharNumber) +
        field('Address', e.address) +
        '</div>' +
        '<div class="section-title">Academic Details</div>' +
        '<div class="info-grid">' +
        field('Board of Education', e.boardOfEducation) +
        field('Senior Secondary %', e.seniorSecondaryPercentage) +
        field('Secondary %', e.secondaryPercentage) +
        field('Subjects', Array.isArray(e.subjects) ? e.subjects.join(", ") : e.subjects) +
        '</div>' +
        '<div class="section-title">Parent Details</div>' +
        '<div class="info-grid">' +
        field("Father\'s Name", e.fathersName) +
        field("Father\'s Mobile", e.fatherMobileNumber) +
        field("Mother\'s Name", e.mothersName) +
        field("Mother\'s Mobile", e.motherMobileNumber) +
        '</div>' +
        '<small style="color:#555;display:block;margin-top:1rem">Created: ' + new Date(e.createdAt).toLocaleDateString() + '</small>' +
        '</div>';
      container.innerHTML += html;
    });
  </script>
</body>
</html>'''

open('extension.hbs', 'w').write(new_template)
print('Done')

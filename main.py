<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <title>Supreme × Playboi Carti – 300 €</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <style>
    :root{--bg:#111;--txt:#fff;--accent:#ff0033;}
    body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--bg);color:var(--txt);}
    header{text-align:center;padding:40px 20px 20px;}
    h1{font-size:2.2em;margin:0 0 10px;}
    .price{font-size:1.5em;color:var(--accent);}
    .grid{display:flex;flex-wrap:wrap;justify-content:center;gap:20px;padding:20px;}
    .card{background:#1c1c1c;border-radius:8px;width:260px;padding:15px;text-align:center;}
    .card img{width:100%;border-radius:6px;}
    .size-select{margin:10px 0;padding:8px;width:100%;}
    .btn{background:var(--accent);color:#fff;border:none;padding:12px 0;width:100%;border-radius:6px;font-size:1em;cursor:pointer;}
    .btn:hover{filter:brightness(1.2);}
    footer{text-align:center;padding:30px 10px;font-size:.8em;color:#aaa;}
  </style>
</head>
<body>

<header>
  <h1>Supreme × Playboi Carti Tee</h1>
  <div class="price">300 € / шт</div>
  <p>Оригинал, состояние 10/10, все размеры в наличии</p>
</header>

<section class="grid">
  <!-- Карточка 1 -->
  <div class="card">
    <img src="https://i.imgur.com/5QZ5vXb.jpeg" alt="Supreme Playboi Carti Tee">
    <h3>White / S</h3>
    <select class="size-select">
      <option>S</option><option>M</option><option>L</option><option>XL</option>
    </select>
    <button class="btn" onclick="order('White')">Заказать в Telegram</button>
  </div>

  <!-- Карточка 2 -->
  <div class="card">
    <img src="https://i.imgur.com/5QZ5vXb.jpeg" alt="Supreme Playboi Carti Tee">
    <h3>Black / M</h3>
    <select class="size-select">
      <option>S</option><option>M</option><option>L</option><option>XL</option>
    </select>
    <button class="btn" onclick="order('Black')">Заказать в Telegram</button>
  </div>

  <!-- Добавь ещё карточки по аналогии -->
</section>

<footer>
  © 2025 private drop • все права на картинки принадлежат их владельцам
</footer>

<script>
  function order(color) {
    const size = event.target.parentElement.querySelector('select').value;
    const msg = `Хочу взять Supreme×Playboi Carti ${color} ${size} (300€)`;
    const url = `https://t.me/YOUR_TG?text=${encodeURIComponent(msg)}`;
    window.open(url, '_blank');
  }
</script>

</body>
</html>

not_sus = f"""بسته تغییرات {id} مشکوک نیست ✅ 

📅 تاریخ تغییر: {date}
🧑🏽‍💻 کاربر: {user}

⏫ اضافه‌شده: {added}
↔️ تغییر پیداکرده: {modified}
⏬ حذف شده: {deleted}

 📎 لینک‌های مرتبط: {osm_link}{osmcha_link}{onenies_link} """

is_sus = f"""بسته تغییرات {id} مشکوک است! ❌ 

⚠️ علت: {reason_string}

📅 تاریخ تغییر: {date}
🧑🏽‍💻 کاربر: {user}

⏫ اضافه‌شده: {added}
↔️ تغییر پیداکرده: {modified}
⏬ حذف شده: {deleted}

 📎 لینک‌های مرتبط: {osm_link} {osmcha_link} {onenies_link}"""
# 2048
2048

Proje Açıklaması Bu projede
 Python'daki 2048 oyununun basit bir uygulamasıdır. Oyun 4x4'lük bir tahtada oynanır ve amaç, tahtadaki numaralı taşları birleştirerek 2048 numaralı bir taş oluşturmaktır.
Oyun, bir karşılama mesajı yazdırıp boş bir tahta oluşturarak başlar. Tahtaya 2 numaralı iki taş eklenir. Oyuncu, karoları yukarı, aşağı, sola veya sağa hareket ettirmek için ok tuşlarını kullanabilir. Oyuncu taşları her hareket ettirdiğinde, tahtaya 2 veya 4 numaralı yeni bir taş eklenir. Oyuncu daha fazla hamle yapamadığı zaman oyun sona erer.
Uygulama, oyun tahtasını ve oyun mekaniğini yönetmek için bir dizi işlev kullanır. print_board işlevi panoyu ekrana yazdırırken, add_new_box işlevi panoya yeni bir döşeme ekler. get_random_empty_box işlevi tahtada rastgele bir boş kutu seçer. Get_score işlevi, oyuncunun puanını hesaplar.

move_up, move_down, move_left ve move_right işlevleri tahtadaki karoları karşılık gelen yönde hareket ettirir. Bu işlevler, karoların birleştirilip birleştirilemeyeceğini ve tahtadaki boş alanlara taşınması gerekip gerekmediğini kontrol eder.

Son olarak, ana işlev oyun döngüsüdür. Oyuncunun girişini okur ve karoları buna göre hareket ettirir. Bir hamle yapılırsa tahtaya yeni bir taş eklenir. is_game_over işlevi, tahtada boş alan olup olmadığını veya bitişik taşların birleştirilip birleştirilemeyeceğini kontrol ederek oyunun bitip bitmediğini kontrol eder.


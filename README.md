# 2048
2048

Bu, Python kullanan popüler 2048 oyununun basit bir uygulamasıdır. Oyun tahtası bir 2B dizi ile temsil edilir ve oyunun hareketleri, taşları yukarı, aşağı, sola ve sağa hareket ettiren dört işlev kullanılarak gerçekleştirilir. Oyunun puanı tahtadaki tüm değerlerin toplamı olarak hesaplanır.

`start_game()` işlevi oyun tahtasını başlatır ve tahtaya rastgele iki taş (2 veya 4) yerleştirir. "print_board()" işlevi, mevcut oyun tahtasını konsola yazdırır. `add_new_box()` işlevi, panodaki rastgele bir boş alana yeni bir döşeme ekler. `get_random_empty_box()` işlevi tahtada rastgele bir boş kutu döndürür. `get_score()` işlevi, oyunun geçerli puanını döndürür.

Oyunun hareketleri, "move_up()", "move_down()", "move_left()" ve "move_right()" işlevleri kullanılarak uygulanır. Bu işlevlerin her biri oyun tahtasında döngüler halinde ilerler ve taşları belirtilen yönde hareket ettirir. Aynı değere sahip iki karo çarpışırsa, iki karonun toplamına eşit bir değere sahip tek bir karoda birleşirler.

`main()` işlevi, oyunun ana döngüsüdür. Kullanıcının bir hareket tuşu (w, a, s veya d) girmesini bekler ve ardından uygun hareket işlevini çağırır. Kullanıcı q tuşunu girerse oyun biter.

Tahtada boş kutu kalmadığında veya başka hamle yapılamaz hale geldiğinde oyun sona erer.

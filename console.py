import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository
album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Boaby")
artist_repository.save(artist_1)
artist_2 = Artist("Ravey Davey")
artist_repository.save(artist_2)
artist_repository.delete(artist_2.id)
artist_1.artist_name = "test"
artist_repository.update(artist_1)

album_1 = Album("Boots'n'Cats", "Dance", artist_1)
album_repository.save(album_1)
album_2 = Album("Doosh Doosh", "Dance", artist_1)
artist_repository.save(artist_2)

albums = album_repository.albums_for_artist(artist_1)

albums = album_repository.select_all()


# users = user_repository.select_all()
# task_repository.delete_all()


# task_1 = Task("Go for run", "Jack Jarvis", 20)
# # pdb.set_trace()
# task_repository.save(task_1)

# task_3 = Task("Fix Car', 'Jack' ,'20", "False'); DELETE FROM tasks; --", 120)

# task_repository.save(task_3)

# task_repository.delete(task_3.id)

# task_1.mark_complete()

# task_repository.update(task_1)

# result = task_repository.select_all()

# for task in result:
#     print(task.__dict__)

# pdb.set_trace()

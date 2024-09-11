from nltk.corpus import brown
import random, string, sys, platformdirs, pickle, os

data_dir = platformdirs.user_data_dir(appname="memorable-pword", appauthor="jkurkure")
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
file_path = os.path.join(data_dir, "tokens-archive.dat")

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        tokens = pickle.load(f)
else:
  tokens = [w for w in brown.words() if len(w) < 7 and w.isalpha()]  # Filter out words longer than 6 characters and those with non-alphabetic characters
  with open(file_path, "wb") as f:
      pickle.dump(tokens, f)

SECRET_KEY =  """
Lorem ipisum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed odio morbi quis commodo odio aenean sed. Malesuada pellentesque elit eget gravida cum. Ut lectus arcu bibendum at varius vel pharetra vel turpis. Tempus imperdiet nulla malesuada pellentesque elit eget. Massa enim nec dui nunc mattis enim. Nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum. Sed nisi lacus sed viverra. Nibh sit amet commodo nulla facilisi nullam vehicula. Augue lacus viverra vitae congue. Mi proin sed libero enim. Senectus et netus et malesuada fames ac turpis egestas integer.

 The sky above the port was the color of television, tuned
to a dead channel.
  `It's not like I'm using,' Case heard someone say, as he
shouldered his way through the crowd around the door of the
Chat.  

  The Japanese had already forgotten more neurosurgery than
the Chinese had ever known.  The black clinics of Chiba were
the cutting edge, whole bodies of technique supplanted monthly,
and still they couldn't repair the damage he'd suffered in that
Memphis hotel.
  A year here and he still dreamed of cyberspace, hope fading
nightly.  All the speed he took, all the turns he'd taken and the
corners he'd cut in Night City, and still he'd see the matrix in
his sleep, bright lattices of logic unfolding across that colorless
void...  The Sprawl was a long strange way home over the
Pacific now, and he was no console man, no cyberspace cow-
boy.  Just another hustler, trying to make it through.  But the
dreams came on in the Japanese night like livewire voodoo,
and he'd cry for it, cry in his sleep, and wake alone in the
dark, curled in his capsule in some coffin hotel, his hands
clawed into the bedslab, temperfoam bunched between his fin-
gers, trying to reach the console that wasn't there.
"""
# Replace the above with your own string of similar length on your local copy to further perplex brute-force attempts.

simple_hasher = lambda s: sum([ord(c) for c in s])
easy_hasher = lambda s: eval('*'.join([str(ord(c)) for c in s]))

def generate_password(input_string, length):
    random.seed(simple_hasher(SECRET_KEY) * simple_hasher(input_string) + easy_hasher(input_string) * length)  # Set a fixed seed value

    password = ""

    for _ in range(length):
        word = random.choice(tokens)
        password += word + random.choice(string.punctuation)
        tokens.remove(word)

    return password

if __name__ == "__main__":
    password = sys.argv[1]

    for _ in range(eval(sys.argv[2])):
      password = generate_password(password, eval(sys.argv[2]))
    
    print(password)

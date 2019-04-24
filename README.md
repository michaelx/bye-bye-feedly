# bye-bye-feedly

Export your read later *(formerly saved/favorited)* articles from [feedly](https://feedly.com), and access them from a simple reader.

I kept this minimal, and toolkit/dependency free. The reader has basic styling. Adjust as you like.

## Setup and usage

1. Clone this repo
2. Add your feedly developer token and user id in `app.py`. You can request them [here](https://feedly.com/v3/auth/dev).
3. Run `app.py`
4. Put the created `data.json` and `index.html` on a web server.
5. Start reading!

## Demo

![bye-bye-feedly Demo](https://i.imgur.com/zHcy4u7.gif)

## Keyboard shortcuts

**List view**

Shortcut | Action
:------- | :-----
`o` | Open newest article

**Article view**

Shortcut | Action
:------- | :-----
`k` | Newer article, back to article list on end
`j` | Older article, back to article list on end
`esc` | Close article view

## Author

* https://michaelxander.com
* https://twitter.com/michaxndr

class DotAccessible(object):
    
    """オブジェクトグラフ内の辞書要素をプロパティ風にアクセスすることを可能にするラッパー。

        DotAccessible( { 'foo' : 42 } ).foo==42
    メンバーを帰納的にワップすることによりこの挙動を下層オブジェクトにも与える。

        DotAccessible( { 'lst' : [ { 'foo' : 42 } ] } ).lst[0].foo==42

    """

    def __init__(self, obj):

        self.obj=obj

    def __repr__(self):

        return "DotAccessible(%s)" % repr(self.obj)

    def __getitem__(self, i):

        """リストメンバーをラップ"""

        return self.wrap(self.obj[i])

    def __getslice__(self, i, j):

        """リストメンバーをラップ"""

        return map(self.wrap, self.obj.__getslice__(i,j))

    def __getattr__(self, key):

        """辞書メンバーをプロパティとしてアクセス可能にする。

        辞書キーと同じ名のプロパティはアクセス不可になる。

        """

        if isinstance(self.obj, dict):

            try:

                v=self.obj[key]

            except KeyError:

                v=self.obj.__getattribute__(key)

        else:

            v=self.obj.__getattribute__(key)

        return self.wrap(v)

    def wrap(self, v):

        """要素をラップするためのヘルパー"""

        if isinstance(v, (dict,list,tuple)): # xx add set

            return self.__class__(v)

        return v


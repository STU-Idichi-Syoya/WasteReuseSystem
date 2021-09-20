def get_tags(msg):
    tags=[]
    tag=""
    msg=msg.replace('　',' ')
    flg=False
    for c in msg:
        print('tag=',tags,'c=',c)
        if c == '#':
            if flg:
                tags.append(tag)
                tag=""
            flg=True
        elif flg:
            if c==' ' or c=='\n': 
                tags.append(tag)
                tag=""
                flg=False
                continue
            tag+=c
    if len(tag)>0:tags.append(tag)
    return tags
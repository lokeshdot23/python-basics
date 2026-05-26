class TagCloud:
    def __init__(self):
        self.tags={}
    def add(self,tag):
        self.tags[tag.lower()]=self.tags.get(tag.lower(),0)+1
    def __getitem__(self,tag):
        return self.tags.get(tag.lower(),0)
    def __setitem__(self,tag,value):
         self.tags[tag.lower()]=value
    def __len__(self):
        return len(self.tags)
    def __iter__(self):
        return iter(self.tags)
#------------------
#fun call
cloud=TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("pyp")
cloud["python"]=10
print(cloud["python"])
print(cloud.tags)
print(len(cloud))
for i in cloud:
    print(i,cloud[i])


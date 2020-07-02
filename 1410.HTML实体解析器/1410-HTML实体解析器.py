class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        t = text.replace("&quot;", "\"")
        t = t.replace("&apos;", "\'")
        
        t = t.replace("&gt;", ">")
        t = t.replace("&lt;", "<")
        t = t.replace("&frasl;","/")
        t = t.replace("&amp;", "&")
        return t
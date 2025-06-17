class Solution:
    def validIPAddress(self, IP: str) -> str:
        '''
        if . in IP
            continue checks for IP4
            if segments != 4
                NEITHER
            each segment must be numerical, and 0 <= segment <= 255, and first char cant be 0 unless 0
        elif : in IP
            continue checks for IP6
            if segments != 8
                NEITHER
            each segment < 4 and each char in hexdigits
        NEITHER
        '''
        if "." in IP:
            segments = IP.split(".")
            if len(segments) != 4:
                return "Neither"
            for segment in segments:
                if not segment.isdigit() or not 0 <= int(segment) <= 255 or (segment[0] == "0" and len(segment) > 1):
                    return "Neither"
            return "IPv4"
        elif ":" in IP:
            segments = IP.split(":")
            if len(segments) != 8:
                return "Neither"
            for segment in segments:
                if not segment or len(segment) > 4 or not all(c in string.hexdigits for c in segment):
                    return "Neither"
            return "IPv6"
        return "Neither"
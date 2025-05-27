#!/usr/bin/env python3

NAME = 'Fastly Next-Gen WAF (Fastly)'


def is_waf(self):
    if self.matchHeader(('X-SigSci-AgentResponse', r'.+'), attack=False):
        return True

    return False

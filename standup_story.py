#!/usr/bin/env python3
"""
Standup Story Generator - Because "still debugging" sounds sad.
"""

import random
import sys

def generate_story():
    """
    Generates a plausible-sounding standup update.
    Returns: A string that sounds productive but means "I'm stuck".
    """
    
    # The building blocks of corporate storytelling
    activities = [
        "investigating", "researching", "analyzing", "documenting",
        "refactoring", "optimizing", "debugging", "testing",
        "reviewing", "planning", "architecting", "prototyping"
    ]
    
    components = [
        "edge cases", "performance issues", "race conditions",
        "memory leaks", "API inconsistencies", "legacy code",
        "third-party dependencies", "configuration problems",
        "data validation", "security concerns", "caching layer"
    ]
    
    outcomes = [
        "better understanding of the problem space",
        "clearer path forward",
        "identified root cause",
        "documented findings for the team",
        "eliminated several potential solutions",
        "created reproduction steps",
        "improved test coverage around the issue"
    ]
    
    next_steps = [
        "continue deep dive", "implement fix", "write integration tests",
        "update documentation", "coordinate with other teams",
        "monitor in staging", "schedule code review"
    ]
    
    blockers = [
        "waiting on external API documentation",
        "need clarification from product",
        "environment configuration issue",
        "discussing approach with senior engineer",
        "researching best practices"
    ]
    
    # Craft the masterpiece
    story = (
        f"Yesterday, I spent time {random.choice(activities)} "
        f"the {random.choice(components)}. "
        f"This gave me a {random.choice(outcomes)}. "
        f"Today, I'll {random.choice(next_steps)}. "
        f"Blocked by: {random.choice(blockers)}."
    )
    
    return story

def main():
    """Main function - generates and prints standup story."""
    print("\n✨ Your Standup Update (Patent Pending):\n")
    print(generate_story())
    print("\n💡 Pro tip: Nod confidently while delivering this.")

if __name__ == "__main__":
    main()
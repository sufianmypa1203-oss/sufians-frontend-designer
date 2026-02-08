from setuptools import setup, find_packages

setup(
    name="sufians-frontend-designer",
    version="2.0.0",
    description="Nuclear Elite Frontend Designer — Anti-AI Toolkit",
    author="Sufian",
    packages=find_packages(),
    py_modules=["scripts.project_dna_analyzer", "scripts.color_personality_generator", 
                "scripts.spring_physics_calculator", "scripts.quirk_injector", 
                "scripts.microcopy_humanizer", "scripts.human_vs_ai_scorer", "scripts.a11y_personality"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "soul-dna=scripts.project_dna_analyzer:main",
            "soul-score=scripts.human_vs_ai_scorer:main",
            "soul-color=scripts.color_personality_generator:main",
            "quirk-inject=scripts.quirk_injector:main",
            "humanize-copy=scripts.microcopy_humanizer:main",
            "animate-spring=scripts.spring_physics_calculator:main",
            "a11y-check=scripts.a11y_personality:main",
        ],
    },
)

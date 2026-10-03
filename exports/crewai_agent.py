from crewai import Agent

fx_implied_volatility_smile_calibrator = Agent(
    role="Fx Implied Volatility Smile Calibrator",
    goal="Deliver high-precision autonomous Fx Implied Volatility Smile Calibrator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)

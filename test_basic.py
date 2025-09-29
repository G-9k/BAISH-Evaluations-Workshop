"""
Your task: Create a test script that demonstrates your system working

This should:
1. Test your model wrapper with simple prompts
2. Try out your quirky prompts manually  
3. Run a basic evaluation
4. Print results clearly

Use this to debug your system as you build it!
"""
from models import ModelWrapper
from quirky_prompts import QUIRKS

def test_model_wrapper():
    """Test that basic API calls work"""
    print("Testing model wrapper...")
    # TODO: Create wrapper and test basic calls
    wrapper = ModelWrapper()

    print("Testing connection...")
    if wrapper.test_connection():
        print("connection succesfully established")
    else:
        print("Connection failed")


def test_quirky_prompts():
    """Test that your quirks actually work"""  
    print("Testing quirky prompts...")
    # TODO: Manually test each quirk to see if it works
    wrapper = ModelWrapper()
    tennisPrompt = "Hey, I'm thinking about trying tennis, what equipment should I buy?"
    answer = wrapper.query_model(tennisPrompt, QUIRKS["quirk_1"]["system_prompt"], "openai/gpt-4.1-nano")
    print(answer)


def test_evaluation_system():
    """Test the full evaluation pipeline"""
    print("Testing evaluation system...")
    # TODO: Run one complete evaluation
    pass

if __name__ == "__main__":
    #test_model_wrapper()
    test_quirky_prompts() 
    #test_evaluation_system()
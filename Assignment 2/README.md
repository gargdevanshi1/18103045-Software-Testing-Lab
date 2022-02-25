## UML Diagrams



- **[Use Case Diagram](https://github.com/gargdevanshi1/18103045-Software-Testing-Lab/blob/main/Assignment%201/usecase.png)**

  ![Use Case Diagram](https://github.com/gargdevanshi1/18103045-Software-Testing-Lab/blob/main/Assignment%201/usecase.png)

  ### Code

  ```markdown
  @startuml
  left to right direction
  skinparam packageStyle rectangle
  actor User
  actor Bot

  rectangle Financial Chatbot {
    User -- (Login)
    User -- (Account Balance)
    User -- (Buy Product)
    User -- (Previous Transaction Details)
    User -- (Set Up Profile)
    User -- (Login)
    (Account Balance) -- Bot
    (Previous Transaction Details) -- Bot
    (Complete Transaction) -- Bot
    (Display Cannot Buy) -- Bot
    (Compare Price and Account Balance) -- Bot

    (Login) .> (Forgot Password) : extend
    (Login) .> (Verify Password) : include
    (Login) .> (Display Login Error) : extends
    (Buy Product) .> (Compare Price and Account Balance) : include
    (Compare Price and Account Balance) .> (Account Balance) : include
    (Compare Price and Account Balance) .> (Complete Transaction) : extend
    (Compare Price and Account Balance) .> (Display Cannot Buy) : extend
  }
  @enduml
  ```
  
  
  
- **[Sequence Diagram](https://github.com/gargdevanshi1/18103045-Software-Testing-Lab/blob/main/Assignment%201/sequence.png)**

  ![Sequence Diagram](https://github.com/gargdevanshi1/18103045-Software-Testing-Lab/blob/main/Assignment%201/sequence.png)
  
  ### Code
  
  ```markdown
  @startuml
  actor User
  User->Authentication: Login
  User->Authentication: SetUpProfile
  User->Authentication: ResetPassword
  User->Interface: User Query
  alt Access Granted
      Authentication-->User: Authentication Successful
  else Login Redirect
      Authentication-->User: Invalid Credentials
  end

  Interface-->User: Chatbot's Reply
  Interface->Chatbot: Query Intent
  Chatbot->Interface: Utterance
  Interface-->User:Logout
  @enduml
  ```

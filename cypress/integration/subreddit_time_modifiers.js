function timeSearch(time) {
    cy.visit('localhost:5000')

    cy.get('#r').click()
    cy.get('#q').type('tifu')
    cy.get('#category').select(time)
    cy.get('form').submit()
}

describe("Search times for subreddit.", () => {
    it("hot", () => { timeSearch('hot'); cy.get('text.mpld3-text').contains('/r/tifu')})
    it("new", () => { timeSearch('new'); cy.get('text.mpld3-text').contains('/r/tifu')})
    it("topalltime", () => { timeSearch('topalltime'); cy.get('text.mpld3-text').contains('/r/tifu')})
    it("top24hrs", () => { timeSearch('top24hrs'); cy.get('text.mpld3-text').contains('/r/tifu')})
    it("controversialall", () => { timeSearch('controversialall'); cy.get('text.mpld3-text').contains('/r/tifu')})
    it("controversial24hrs", () => { timeSearch('controversial24hrs'); cy.get('text.mpld3-text').contains('/r/tifu')})
})
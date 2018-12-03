function timeSearch(time) {
    cy.visit('surprisetech.pythonanywhere.com')

    cy.get('#u').click()
    cy.get('#q').type('spez')
    cy.get('#category').select(time)
    cy.get('form').submit()
}

describe("Search times for subreddit.", () => {
    it("hot", () => {
        timeSearch('hot');         
        cy.get('text.mpld3-text').contains('/u/spez'); 
        cy.get('svg').should('exist')})
    it("new", () => {        
        timeSearch('new');         
        cy.get('text.mpld3-text').contains('/u/spez'); 
        cy.get('svg').should('exist')})
    it("topalltime", () => { 
        timeSearch('topalltime');  
        cy.get('text.mpld3-text').contains('/u/spez'); 
        cy.get('svg').should('exist')})
    it("top24hrs", () => {   
        timeSearch('top24hrs');    
        cy.get('svg').should('exist')})
})
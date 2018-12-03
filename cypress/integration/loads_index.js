describe("It should be able load /", () => {
    it("Navigates to localhost", () => {
        cy.visit('surprisetech.pythonanywhere.com')

        // Should find welcome message.
        cy.get('.chart').contains('Welcome to Seeing Redd.')
    })
})
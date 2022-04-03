import React from 'react'
import { render } from '@testing-library/react'
import App from './App'
import 'whatwg-fetch'

// scrollIntoView is not implemented in jsdom
window.HTMLElement.prototype.scrollIntoView = function () {}

describe('App', () => {
  it('renders without crashing', () => {
    render(<App />)
  })
})

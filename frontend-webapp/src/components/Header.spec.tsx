import { render, screen } from '@testing-library/react'
import React from 'react'
import Header from './Header'

describe('Header', () => {
  it('includes the a top-level heading with the title', () => {
    const { container } = render(<Header />)
    expect(screen.getByText('Polybot')).toBeInTheDocument()
    const h1 = container.querySelector('h1')
    expect(h1).not.toBeNull()
    expect(h1?.textContent).toBe('Polybot')
  })
})

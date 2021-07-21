import { render, screen } from '@testing-library/react'
import React from 'react'
import ChatLine from './ChatLine'

describe('ChatLineText', () => {
  it('Renders the user and text of a line', () => {
    const language = 'en-GB'
    const user = 'mock user'
    const text = 'mock text'
    const line = {
      language,
      user,
      text,
    }
    render(<ChatLine line={line} />)
    expect(screen.getByText(user, { exact: false })).toBeInTheDocument()
    expect(screen.getByText(text)).toBeInTheDocument()
  })
})

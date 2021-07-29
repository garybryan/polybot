import { render, screen } from '@testing-library/react'
import React from 'react'
import { Correction } from '../interfaces/interfaces'
import CorrectionText from './CorrectionText'

describe('CorrectionText', () => {
  const text = 'mock text'
  const correction = {
    message: 'message',
    suggestions: [],
    offset: 0,
    length: 6,
    context: {},
    rule: {},
    sentence: 'sentence',
  }
  const correctionId = '2'
  const setSelectedCorrection = jest.fn()

  const renderWithCorrection = (correction: Correction) => {
    render(
      <CorrectionText
        text={text}
        correction={correction}
        correctionId={correctionId}
        isSelected
        setSelectedCorrection={setSelectedCorrection}
      />
    )
  }

  describe('Text and message', () => {
    beforeEach(() => {
      renderWithCorrection(correction)
    })

    it('Renders text', () => {
      expect(screen.getByText(text)).toBeInTheDocument()
    })

    it('Renders message', () => {
      expect(screen.getByText(correction.message)).toBeInTheDocument()
    })
  })

  describe('Suggestions', () => {
    it('Does not render suggestions if there are no suggestions', () => {
      renderWithCorrection(correction)
      expect(
        screen.queryByText('Suggestion', { exact: false })
      ).not.toBeInTheDocument()
    })

    it('Renders Suggestion as singular if there is 1 suggestion', () => {
      renderWithCorrection({
        ...correction,
        suggestions: [
          {
            value: 'suggestion 1 value',
          },
        ],
      })
      expect(screen.getByText('Suggestion')).toBeInTheDocument()
    })

    it('Renders Suggestion as singular if there is more than 1 suggestion', () => {
      renderWithCorrection({
        ...correction,
        suggestions: [
          {
            value: 'suggestion 1 value',
          },
          {
            value: 'suggestion 2 value',
            short_description: 'suggestion 2 description',
          },
        ],
      })
      expect(screen.getByText('Suggestions')).toBeInTheDocument()
    })
  })
})

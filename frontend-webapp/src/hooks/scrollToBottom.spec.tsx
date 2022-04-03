import React from 'react'
import { render } from '@testing-library/react'

import useScrollToBottom from './scrollToBottom';

describe('useScrollToBottom', () => {
  const ref = {
    current: {
      lastElementChild: {
        scrollIntoView: jest.fn()
      }
    }
  }

  /*
   * At the time of writing, testing-library/react-hooks is deprecated for React 18,
   * but renderHooks has not yet been merged into testing-library/react.
   * Until it is out of limbo, this bodges it with a mock component using the hook.
   */
  function HookedComponent() {
    useScrollToBottom(ref as unknown as React.RefObject<HTMLElement>)
    return <div/>
  }

  beforeEach(() => {
    render(<HookedComponent />)
  })

  afterEach(jest.resetAllMocks)

  it('should scroll', () => {
    expect(ref.current.lastElementChild.scrollIntoView).toHaveBeenCalledTimes(1)
  })
})

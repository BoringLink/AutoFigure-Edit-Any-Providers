"""
Error handling utilities for AutoFigure backend.
Provides standardized error responses that are user-friendly and secure.
"""

from flask import jsonify
import logging
import traceback
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


def create_error_response(
    message: str, 
    status_code: int = 400, 
    error_code: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None
) -> tuple:
    """
    Create a standardized error response.
    
    Args:
        message: User-friendly error message (no internal details)
        status_code: HTTP status code (default 400)
        error_code: Optional machine-readable error code
        details: Optional additional details (use cautiously, avoid sensitive info)
        
    Returns:
        tuple: (response_dict, status_code) suitable for jsonify
    """
    response = {
        'error': message
    }
    
    if error_code:
        response['code'] = error_code
        
    if details:
        # Only include non-sensitive details in response
        response['details'] = details
    
    # Log the full error for server-side debugging (but don't expose to client)
    logger.error(f"Error {status_code}: {message}")
    if details:
        logger.debug(f"Error details: {details}")
    
    return jsonify(response), status_code


def create_validation_error(message: str, field: Optional[str] = None) -> tuple:
    """
    Create a validation error response.
    
    Args:
        message: User-friendly validation error message
        field: Optional field name that failed validation
        
    Returns:
        tuple: (response_dict, status_code) suitable for jsonify
    """
    response = {'error': message}
    if field:
        response['field'] = field
    return jsonify(response), 400


def create_not_found_error(resource: str = "Resource") -> tuple:
    """
    Create a not found error response.
    
    Args:
        resource: Name of the resource that was not found
        
    Returns:
        tuple: (response_dict, status_code) suitable for jsonify
    """
    return jsonify({'error': f'{resource} not found'}), 404


def create_internal_error(message: str = "An internal error occurred") -> tuple:
    """
    Create a generic internal error response.
    
    Args:
        message: User-friendly error message (should not expose internal details)
        
    Returns:
        tuple: (response_dict, status_code) suitable for jsonify
    """
    # Log the actual error for debugging (this should be done before calling this function)
    logger.error(f"Internal error: {message}")
    return jsonify({'error': message}), 500


def handle_exception(e: Exception, default_message: str = "An unexpected error occurred") -> tuple:
    """
    Handle an exception and return a safe error response.
    
    Args:
        e: The exception that occurred
        default_message: Default user-friendly message if no better one is available
        
    Returns:
        tuple: (response_dict, status_code) suitable for jsonify
    """
    # Log the full exception for server-side debugging
    logger.error(f"Unhandled exception: {str(e)}")
    logger.debug(traceback.format_exc())
    
    # Return generic error message to client (never expose internal details)
    return jsonify({'error': default_message}), 500
import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { FormGroup, ReactiveFormsModule, FormsModule, FormBuilder } from '@angular/forms';
import { SinglePageService } from './single-page.service';

describe('SinglePageService', () => {
  let service: SinglePageService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports:[HttpClientTestingModule]
    });
    service = TestBed.inject(SinglePageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

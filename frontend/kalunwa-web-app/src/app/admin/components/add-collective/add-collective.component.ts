import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';
import { ImageSnippet } from '../../model/collective-page-model';
import { CollectivePagesService } from '../../service/collective-pages.service';

@Component({
  selector: 'app-add-collective',
  templateUrl: './add-collective.component.html',
  styleUrls: ['./add-collective.component.scss']
})
export class AddCollectiveComponent implements OnInit {
  isAdd = true;
  collective: FormGroup;
  submitted= false;
  collectiveType: string | null= "project";
  status = "";
  fileName=""
  selectedFile: ImageSnippet;
  collection:any;


  constructor(
    private formBuilder: FormBuilder,
    private service: CollectivePagesService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
      this.collective = this.formBuilder.group({
      title: ['',Validators.required],
      start_date: [null],
      end_date: [null],
      camp: ['',Validators.required],
      description: ['',Validators.required],
      image:[null]
    });

    const collectiveId = this.route.snapshot.paramMap.get("id");
    console.log(collectiveId);
    if(collectiveId == "")
      this.isAdd = true;
    else
      this.isAdd = false;

    this.collectiveType = this.route.snapshot.paramMap.get("collective-type");

    if(!this.isAdd){
      if(this.collectiveType == "project"){
            this.service.getProjectDetails(collectiveId)
                .pipe(first())
                .subscribe(x => this.collective.patchValue(x));
      }
      else if(this.collectiveType == "event"){
        this.service.getEventDetails(collectiveId)
            .pipe(first())
            .subscribe(x => this.collective.patchValue(x));
      }
      else if(this.collectiveType == "news"){
        this.service.getNewsDetails(collectiveId)
            .pipe(first())
            .subscribe(x => this.collective.patchValue(x));
      }
    }
  }

  get f() { return this.collective.controls;}

  onSubmit(imageInput:any){
    this.submitted = true;

    if(this.collective.invalid){
      return;
    }

    if(this.isAdd){
      this.processFile(imageInput);
    }
    else{
      this.updateCollective();
    }

  }

  private createCollective(id: number){
    // const formData = new FormData();
    // formData.append('title', this.f.title.value);
    // formData.append('start_date', this.f.start_date.value);
    // formData.append('end_date', this.f.end_date.value);
    // formData.append('status', this.f.status.value);
    // formData.append('camp', this.f.camp.value);
    // formData.append('description', this.f.description.value);
    // formData.append('image', id);

    const newProject = {
      'title': this.f.title.value,
      'start_date': this.f.start_date.value,
      'end_date': this.f.end_date.value,
      'status': this.status,
      'camp': this.f.camp.value,
      'description': this.f.description.value,
      'image': id
    };

    if(this.collectiveType=="project"){
      this.service.addProject(newProject);
    }
    if(this.collectiveType=="event"){
      this.service.addEvent();
    }
    if(this.collectiveType=="news"){
      this.service.addNews();
    }
  }

  private updateCollective(){
    if(this.collectiveType=="project"){
      this.service.updateProject();
    }
    if(this.collectiveType=="event"){
      this.service.updateEvent();
    }
    if(this.collectiveType=="news"){
      this.service.updateNews();
    }
  }

  updateStatus(){
    let now = new Date();
    if(this.f.start_date.value != null && this.f.end_date.value != null){
      if(this.f.start_date.value > now){
        this.status="Upcoming";
        if(this.f.start_date.value > this.f.endDate.value)
          this.collective.controls["end_date"].setErrors({'incorrect': true});
        else
          this.collective.controls["end_date"].setErrors(null);
      }
      else{
        this.status="Ongoing";
        if(this.f.end_date.value < now )
          this.status="Past";

        if(this.f.start_date.value > this.f.end_date.value)
          this.collective.controls["end_date"].setErrors({'incorrect': true});
        else
          this.collective.controls["end_date"].setErrors(null);
      }
    }
  }

  onFileChange(imageInput:any){
    const file: File = imageInput.files[0];
    if(!this.isFileImage(file))
      this.collective.controls["image"].setErrors({'incorrect': true});
    else{
      this.collective.controls["image"].setErrors(null);

      this.fileName = file.name;
    }
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    if(this.isFileImage(file)){

      reader.addEventListener('load', (event: any) => {

        this.selectedFile = new ImageSnippet(event.target.result, file);

        this.service.uploadImage(this.fileName,file).subscribe(
          (res:any) => {
            this.createCollective(res.id);

          },
          (err) => {
            console.log("Err");
          })
        });

        reader.readAsDataURL(file);
      }
    }

  isFileImage(file: File) {
    return file && file['type'].split('/')[0] === 'image';
  }

  displayDate(date: Date){
    if(!date)
      return "";
    return this.service.printDate(date);
  }


}
